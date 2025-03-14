import sys, os, io
from typing import List, Dict
from treelib import Tree

class FileExplorer:
    def __init__(self, root_path: str, config: Dict):
        self.root_path = root_path
        self.exclude_folders = [folder.lower() for folder in config.get("exclude_folders", [])]
        self.exclude_files = [file.lower() for file in config.get("exclude_files", [])]
        self.allowed_extensions = [ext.lower() for ext in config.get("allowed_extensions", [])]
        self.results = {}

    def explore(self) -> Dict[str, str]:
        self._traverse_directory(self.root_path)
        return self.results

    # 폴더 탐색
    def _traverse_directory(self, current_path: str):
        try:
            for item in os.listdir(current_path):
                item_path = os.path.join(current_path, item)
                item_name = os.path.basename(item_path).lower()

                if os.path.isdir(item_path):
                    if item_name in self.exclude_folders:
                        continue
                    self._traverse_directory(item_path)
                elif os.path.isfile(item_path):
                    if item_name in self.exclude_files:
                        continue
                    _, ext = os.path.splitext(item)
                    if ext.lower() in self.allowed_extensions:
                        try:
                            with open(item_path, 'r', encoding='utf-8') as file:
                                content = file.read()
                                self.results[item_path] = content
                        except Exception as e:
                            self.results[item_path] = f"Error reading file: {str(e)}"
        except PermissionError:
            print(f"Permission denied: {current_path}")
        except Exception as e:
            print(f"Error exploring {current_path}: {str(e)}")

    # 디렉터리 구조 시각화
    def visualize_file_tree(self, file_paths: List[str], root_path: str):
        tree = Tree()
        tree.create_node(root_path, root_path)
        for file_path in file_paths:
            relative_path = os.path.relpath(file_path, root_path)
            path_parts = relative_path.split(os.sep)
            current_path = root_path
            for i, part in enumerate(path_parts):
                parent_path = current_path
                current_path = os.path.join(current_path, part)
                if not tree.contains(current_path):
                    tree.create_node(part, current_path, parent=parent_path)
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        tree.show()
        tree_str = new_stdout.getvalue()
        sys.stdout = old_stdout
        return tree_str