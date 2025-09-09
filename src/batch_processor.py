#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF批处理模块
负责批量处理多个PDF文件
"""

import os
import pandas as pd
from .pdf_processor import PDFProcessor


class BatchProcessor:
    """PDF批处理器类，负责批量处理多个PDF文件"""
    
    def __init__(self):
        """初始化批处理器"""
        self.pdf_processor = PDFProcessor()
        self.error_log = []
    
    def process_folder(self, src_folder, dst_folder, excel_path, password):
        """
        批量处理文件夹中的PDF文件
        
        Args:
            src_folder (str): 源文件夹路径
            dst_folder (str): 目标文件夹路径
            excel_path (str): Excel文件路径（包含稿件编号和方向信息）
            password (str): PDF加密密码
        """
        try:
            # 创建目标文件夹
            if not os.path.exists(dst_folder):
                os.makedirs(dst_folder)
            
            # 读取Excel文件
            paper_data = self._load_paper_data(excel_path)
            
            # 获取源文件夹中的所有文件
            src_files = [f for f in os.listdir(src_folder) if f.lower().endswith('.pdf')]
            
            if not src_files:
                print("源文件夹中没有找到PDF文件")
                return
            
            print(f"找到 {len(src_files)} 个PDF文件，开始处理...")
            
            # 处理每个PDF文件
            for i, src_file in enumerate(src_files, 1):
                try:
                    print(f"正在处理 ({i}/{len(src_files)}): {src_file}")
                    
                    # 从文件名提取稿件编号
                    paper_code = src_file.split('_')[0]
                    
                    # 获取研究方向
                    if paper_code in paper_data:
                        direction = paper_data[paper_code]
                        paper_info = (paper_code, direction)
                        
                        # 构建文件路径
                        src_pdf = os.path.join(src_folder, src_file)
                        dst_pdf = os.path.join(dst_folder, src_file)
                        
                        # 处理PDF
                        self.pdf_processor.add_headers_and_footers(
                            src_pdf, dst_pdf, paper_info, password
                        )
                        
                        print(f"✓ 成功处理: {src_file}")
                    else:
                        error_msg = f"未找到稿件编号 {paper_code} 对应的研究方向"
                        print(f"✗ {error_msg}")
                        self.error_log.append(f"{src_file}: {error_msg}")
                        
                except Exception as e:
                    error_msg = f"处理文件时出错: {str(e)}"
                    print(f"✗ {error_msg}")
                    self.error_log.append(f"{src_file}: {error_msg}")
            
            # 保存错误日志
            if self.error_log:
                self._save_error_log()
            
            print(f"\n批处理完成！成功处理 {len(src_files) - len(self.error_log)} 个文件")
            if self.error_log:
                print(f"处理失败 {len(self.error_log)} 个文件，详见 error_log.txt")
                
        except Exception as e:
            print(f"批处理过程中出现错误: {str(e)}")
    
    def _load_paper_data(self, excel_path):
        """
        从Excel文件加载稿件数据
        
        Args:
            excel_path (str): Excel文件路径
            
        Returns:
            dict: 稿件编号到研究方向的映射
        """
        try:
            df = pd.read_excel(excel_path)
            paper_data = {}
            
            for i in range(df.shape[0]):
                paper_code = df.iloc[i, 0]
                direction = df.iloc[i, 1]
                paper_data[paper_code] = direction
            
            print(f"成功加载 {len(paper_data)} 条稿件数据")
            return paper_data
            
        except Exception as e:
            raise Exception(f"读取Excel文件失败: {str(e)}")
    
    def _save_error_log(self):
        """保存错误日志到文件"""
        try:
            with open('error_log.txt', 'w', encoding='utf-8') as f:
                for error in self.error_log:
                    f.write(error + '\n')
            print("错误日志已保存到 error_log.txt")
        except Exception as e:
            print(f"保存错误日志失败: {str(e)}")
