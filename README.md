<div align="center">
	<h1>CopyAllDir</h1>
		<a href="https://github.com/penguinhing/CopyAllDir/releases/tag/v1.0">
		<img src="https://img.shields.io/github/v/release/penguinhing/CopyAllDir?color=4CAF50" alt="GitHub release">
	</a>
		<a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
	</a>
</div>

<br/><br/><br/><br/><br/><br/>
## 제작 목적
- AI에게 코드 분석이나 개선을 요청하고 싶을 때, 매번 전체 코드를 복사해서 붙이는 번거로움을 줄이기 위해 제작
<br/><br/><br/>

## 사용 방법
1. **설치**: Installer를 통해 프로그램을 설치합니다.
2. **기능 실행**: 폴더를 우클릭한 후 나타나는 메뉴에서 `CopyAllDir`를 선택하면 두 가지 옵션이 제공됩니다:
   - **복사 설정**: 복사할 대상을 설정합니다.
   - **디렉터리 구조 및 코드 전체 복사**: 설정된 복사 조건에 따라 디렉터리 구조와 코드를 복사합니다.


#### 복사 설정
- 복사 대상을 지정하는 옵션입니다.
- 여러 파라미터를 입력할 경우, 반드시 쉼표(`,`)로 구분해야 하며 공백은 포함시키지 않습니다.


#### 디렉터리 구조 및 코드 전체 복사
- '복사 설정'에서 정의한 조건에 따라 디렉터리 구조와 모든 코드를 복사합니다.

<br/><br/><br/>

## 실제 사용 예시
![Image](https://github.com/user-attachments/assets/b4c162e0-22ba-4241-aefb-5eff4f4ba0c7)


## 복사 내용 예시
```
전체 디렉터리 구조:
C:\workspace\python\CopyAllDir
├── lib
│   ├── explorer.py
│   └── setting.py
└── main.py




====================
파일 경로: C:\workspace\python\CopyAllDir\lib\explorer.py
파일 내용:
import sys, os, io
from typing import List, Dict
from treelib import Tree

class FileExplorer:
    ...
	
====================
파일 경로: C:\workspace\python\CopyAllDir\lib\setting.py
파일 내용:
 ...
```

