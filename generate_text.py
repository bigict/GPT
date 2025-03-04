# generate_text.py
import sys
import os

# 添加当前目录到路径，确保可以导入language_model包
sys.path.insert(0, os.path.abspath('.'))

from gpt.generate import main

if __name__ == "__main__":
    main()