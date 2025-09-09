#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF批处理工具主程序
"""

import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui import PDFProcessorGUI


def main():
    """主函数"""
    print("启动PDF批处理工具...")
    
    try:
        # 创建并运行GUI
        app = PDFProcessorGUI()
        app.run()
    except Exception as e:
        print(f"程序启动失败: {str(e)}")
        input("按回车键退出...")


if __name__ == '__main__':
    main()
