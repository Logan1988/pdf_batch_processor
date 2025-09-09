#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF批处理工具快速启动脚本
"""

import sys
import os

# 确保可以找到模块
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

if __name__ == '__main__':
    from main import main
    main()
