import os
import sys
import pyperclip
import json
from typing import Dict
from lib.setting import SettingsGUI
from lib.explorer import FileExplorer

def load_config(config_path) -> Dict:
    default_config = {
        "exclude_folders": ["env", "__pycache__", "build", "dist"],
        "exclude_files": [],
        "allowed_extensions": [".txt", ".py", ".reg"]
    }
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                pass
    return default_config

def get_run_path():
    if getattr(sys, 'frozen', False):  # EXE로 실행 중일 때
        return os.path.abspath(sys.executable)
    else:
        return os.path.abspath(__file__)
    

if __name__ == "__main__":
    config_path = os.path.dirname(get_run_path()) + "\\config.json"
    print(config_path)
    config = load_config(config_path)

    if len(sys.argv) < 2:
        input("Error: Please specify the folder path")
        sys.exit(1)

    root_path = sys.argv[1]
   
    #  설정 GUI 실행
    if len(sys.argv) > 2 and sys.argv[2] == "/settings":
        SettingsGUI(config_path, config)
        sys.exit(0)


    # 기본 동작: 설정 로드 후 바로 복사
    explorer = FileExplorer(root_path, config)
    results = explorer.explore()

    file_paths = list(results.keys())
    result_text = "전체 디렉터리 구조:\n"
    result_text += explorer.visualize_file_tree(file_paths, root_path)
    result_text += "\n" * 3
    for path, content in results.items():
        result_text += "=" * 20
        result_text += f"\n파일 경로: {path}\n"
        result_text += f"파일 내용:\n{content}\n"
    
    pyperclip.copy(result_text)
    print("Results have been copied to clipboard!")