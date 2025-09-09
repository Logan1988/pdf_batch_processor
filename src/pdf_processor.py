#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF批处理核心功能模块
包含添加页眉页脚、加密等核心功能
"""

import os
import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import cm


class PDFProcessor:
    """PDF处理器类，负责处理PDF文件的页眉页脚添加和加密"""
    
    def __init__(self):
        """初始化PDF处理器"""
        # 注册中文字体 - 字体文件在pdf_processor目录下
        font_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'STSONG.TTF')
        if os.path.exists(font_path):
            pdfmetrics.registerFont(TTFont('song', font_path))
            print(f"成功加载字体文件: {font_path}")
        else:
            print(f"警告: 字体文件 {font_path} 不存在，将使用默认字体")
            # 如果字体文件不存在，尝试使用系统字体
            try:
                pdfmetrics.registerFont(TTFont('song', '/System/Library/Fonts/STSong.ttc'))
                print("使用系统默认中文字体")
            except:
                print("警告: 无法加载中文字体，可能出现中文显示问题")
    
    def add_headers_and_footers(self, src_pdf, dst_pdf, paper_info, password):
        """
        为PDF添加页眉页脚并加密
        
        Args:
            src_pdf (str): 源PDF文件路径
            dst_pdf (str): 目标PDF文件路径
            paper_info (tuple): 稿件信息 (稿件编号, 研究方向)
            password (str): PDF加密密码
        """
        try:
            # 读取已有的PDF
            target_pdf = PdfFileReader(open(src_pdf, "rb"))
            num_pages = target_pdf.getNumPages()
            
            # 创建PDF写入器
            output_writer = PdfFileWriter()
            
            for i in range(num_pages):
                # 加载原始PDF的每一页
                src_page = target_pdf.getPage(i)
                
                # 创建临时PDF文件
                temp_file = 'temp.pdf'
                self._create_page_overlay(temp_file, paper_info, i + 1)
                
                # 合并页面
                new_pdf = PdfFileReader(temp_file)
                src_page.mergePage(new_pdf.getPage(0))
                output_writer.addPage(src_page)
                
                # 删除临时文件
                os.remove(temp_file)
            
            # 加密PDF   只允许打印，不允许复制和修改
            output_writer.encrypt(user_pwd='', owner_pwd=password,permissions_flag=4)
            
            # 输出处理后的PDF
            with open(dst_pdf, 'wb') as output_stream:
                output_writer.write(output_stream)
                
        except Exception as e:
            raise Exception(f"处理PDF文件时出错: {str(e)}")
    
    def _create_page_overlay(self, temp_file, paper_info, page_num):
        """
        创建页面覆盖层，包含页眉页脚
        
        Args:
            temp_file (str): 临时文件路径
            paper_info (tuple): 稿件信息 (稿件编号, 研究方向)
            page_num (int): 页码
        """
        # 设置画布
        c = canvas.Canvas(temp_file, pagesize=A4)
        
        # 绘制白色矩形覆盖原有页眉页脚
        c.setStrokeColor('white')
        c.setFillColor('white')
        c.rect(10, 27.7*cm, 21*cm, 72, fill=1)  # 覆盖页眉，上边距2cm
        c.rect(10, 0, 21*cm, 2.5*cm, fill=1)   # 覆盖页脚，下边距3cm
        
        # 设置字体和颜色
        c.setFillColor('black')
        c.setFont('song', 8)
        
        # 添加页眉内容
        c.drawString(72, 816, '中国企业管理案例与质性研究论坛(2021)候审稿件')
        c.drawString(72, 806, f'稿件编号：{paper_info[0]}')
        
        # 添加研究方向（右对齐）
        right_x = self._calculate_right_position(paper_info[1])
        c.drawString(right_x, 806, paper_info[1])
        
        # 添加页码
        c.drawString(295, 25.5, str(page_num))
        
        c.save()
    
    def _calculate_right_position(self, text):
        """
        计算右对齐文本的位置
        
        Args:
            text (str): 要右对齐的文本
            
        Returns:
            float: 文本的x坐标位置
        """
        text_width = stringWidth(text, 'song', 8)
        right_x = 525.3 - text_width
        return right_x
