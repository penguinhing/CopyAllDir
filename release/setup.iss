[Setup]
AppName=CopyAllDir
AppVersion=1.0
DefaultDirName={pf}\CopyAllDir
OutputDir=C:\Output
OutputBaseFilename=CopyAllDir_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\workspace\python\CopyAllDir\release\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Registry]
Root: HKCR; Subkey: "Directory\shell\CopyAllDir"; ValueType: string; ValueName: ""; ValueData: "CopyAllDir"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\shell\CopyAllDir"; ValueType: string; ValueName: "ExtendedSubCommandsKey"; ValueData: "Directory\\ContextMenus\\CopyAllDir"
Root: HKCR; Subkey: "Directory\ContextMenus\CopyAllDir"; ValueType: none; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\ContextMenus\CopyAllDir\shell\CopyStructure"; ValueType: string; ValueName: ""; ValueData: "디렉터리 구조 및 코드 전체 복사"
Root: HKCR; Subkey: "Directory\ContextMenus\CopyAllDir\shell\CopyStructure\command"; ValueType: string; ValueName: ""; ValueData: """{pf}\CopyAllDir\copy_all_dir.exe"" ""%1"""
Root: HKCR; Subkey: "Directory\ContextMenus\CopyAllDir\shell\Settings"; ValueType: string; ValueName: ""; ValueData: "복사 설정"
Root: HKCR; Subkey: "Directory\ContextMenus\CopyAllDir\shell\Settings\command"; ValueType: string; ValueName: ""; ValueData: """{pf}\CopyAllDir\copy_all_dir.exe"" ""%1"" /settings"