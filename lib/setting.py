import json
import tkinter as tk
from tkinter import messagebox


class SettingsGUI:
    def __init__(self, config_path: str, config):
        self.config_path = config_path
        self.config = config
        self.root = tk.Tk()
        self.root.title("복사 설정")
        self.root.geometry("400x500")

        tk.Label(self.root, text="제외 폴더:").pack(pady=5)
        self.exclude_folders_var = tk.StringVar(value=",".join(self.config.get("exclude_folders", [])))
        tk.Entry(self.root, textvariable=self.exclude_folders_var, width=50).pack()

        tk.Label(self.root, text="제외 파일:").pack(pady=5)
        self.exclude_files_var = tk.StringVar(value=",".join(self.config.get("exclude_files", [])))
        tk.Entry(self.root, textvariable=self.exclude_files_var, width=50).pack()

        tk.Label(self.root, text="허용 확장자:").pack(pady=5)
        self.allowed_extensions_var = tk.StringVar(value=",".join(self.config.get("allowed_extensions", [])))
        tk.Entry(self.root, textvariable=self.allowed_extensions_var, width=50).pack()

        tk.Button(self.root, text="저장", command=self.save_config).pack(pady=20)

        self.root.mainloop()

    def save_config(self):
        config = {
            "exclude_folders": self.exclude_folders_var.get().split(","),
            "exclude_files": self.exclude_files_var.get().split(","),
            "allowed_extensions": self.allowed_extensions_var.get().split(",")
        }
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)
        messagebox.showinfo("성공", "설정이 저장되었습니다!")
        self.root.destroy()