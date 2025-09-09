#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF批处理GUI界面模块
提供简单的图形用户界面
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import os
from .batch_processor import BatchProcessor


class PDFProcessorGUI:
    """PDF批处理GUI类"""
    
    def __init__(self):
        """初始化GUI"""
        self.root = tk.Tk()
        self.batch_processor = BatchProcessor()
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        self.root.title("PDF批处理工具")
        self.root.geometry('700x600')
        
        # 设置深色主题
        self.root.configure(bg='#1e1e1e')
        
        # 设置窗口居中
        self.center_window()
        
        # 创建输入框和标签
        self.create_widgets()
    
    def center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        width = 700
        height = 800
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """创建界面组件"""
        # 标题
        title_label = tk.Label(
            self.root, 
            text="PDF批处理工具", 
            font=("Arial", 20, "bold"),
            bg='#1e1e1e',
            fg='#ffffff'
        )
        title_label.pack(pady=30)
        
        # 创建主容器
        main_container = tk.Frame(self.root, bg='#1e1e1e')
        main_container.pack(expand=True, fill='both', padx=40, pady=20)
        
        # 源文件夹选择
        self.create_input_section(
            main_container,
            "待处理文件夹地址：", 
            "src_folder", 
            "选择包含PDF文件的文件夹",
            "blue"
        )
        
        # 目标文件夹选择
        self.create_input_section(
            main_container,
            "处理后保存地址：", 
            "dst_folder", 
            "选择保存处理后PDF的文件夹",
            "green"
        )
        
        # Excel文件选择
        self.create_input_section(
            main_container,
            "Excel文件路径：", 
            "excel_file", 
            "选择包含稿件信息的Excel文件",
            "orange",
            [("Excel files", "*.xlsx"), ("Excel files", "*.xls")]
        )
        
        # 密码输入
        self.create_password_section(main_container)
        
        # 页眉文本输入
        self.create_text_input(
            main_container,
            "页眉文本：", 
            "header_text", 
            "中国企业管理案例与质性研究论坛(2021)候审稿件"
        )
        
        # 处理按钮
        process_btn = tk.Button(
            main_container, 
            text="🚀 开始处理", 
            command=self.start_processing,
            bg="white",
            fg="black",
            font=("Arial", 16, "bold"),
            height=3,
            width=20,
            relief="raised",
            bd=3,
            activebackground="#f0f0f0",
            activeforeground="black"
        )
        process_btn.pack(pady=40)
        
        # 状态标签
        self.status_label = tk.Label(
            main_container, 
            text="请填写所有必要信息后点击开始处理", 
            fg="#00BCD4",
            bg='#1e1e1e',
            font=("Arial", 12)
        )
        self.status_label.pack(pady=10)
    
    def create_input_section(self, parent, label_text, var_name, dialog_title, button_color, filetypes=None):
        """创建输入区域"""
        # 主框架
        section_frame = tk.Frame(parent, bg='#1e1e1e')
        section_frame.pack(fill='x', pady=15)
        
        # 标签
        label = tk.Label(section_frame, text=label_text, 
                        font=("Arial", 12, "bold"), 
                        bg='#1e1e1e', fg='#ffffff',
                        anchor="w")
        label.pack(fill='x', pady=(0, 5))
        
        # 输入框和按钮的框架
        input_frame = tk.Frame(section_frame, bg='#1e1e1e')
        input_frame.pack(fill='x')
        
        # 输入框
        setattr(self, f"{var_name}_var", tk.StringVar())
        entry = tk.Entry(input_frame, textvariable=getattr(self, f"{var_name}_var"), 
                        font=("Arial", 11), bg='#2d2d2d', fg='#ffffff', 
                        insertbackground='#ffffff', relief="sunken", bd=2,
                        width=60)
        entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # 浏览按钮 - 白色背景，黑色文字
        if filetypes:
            browse_btn = tk.Button(
                input_frame, 
                text="📁 浏览文件", 
                command=lambda: self.browse_file(var_name, dialog_title, filetypes),
                bg="white",
                fg="black",
                font=("Arial", 10, "bold"),
                width=12,
                height=1,
                relief="raised",
                bd=2,
                activebackground="#f0f0f0",
                activeforeground="black"
            )
        else:
            browse_btn = tk.Button(
                input_frame, 
                text="📁 浏览文件夹", 
                command=lambda: self.browse_folder(var_name, dialog_title),
                bg="white",
                fg="black",
                font=("Arial", 10, "bold"),
                width=12,
                height=1,
                relief="raised",
                bd=2,
                activebackground="#f0f0f0",
                activeforeground="black"
            )
        browse_btn.pack(side="right")
    
    def create_password_section(self, parent):
        """创建密码输入区域"""
        # 主框架
        section_frame = tk.Frame(parent, bg='#1e1e1e')
        section_frame.pack(fill='x', pady=15)
        
        # 标签
        label = tk.Label(section_frame, text="PDF密码：", 
                        font=("Arial", 12, "bold"), 
                        bg='#1e1e1e', fg='#ffffff',
                        anchor="w")
        label.pack(fill='x', pady=(0, 5))
        
        # 密码输入框
        self.password_var = tk.StringVar()
        entry = tk.Entry(section_frame, textvariable=self.password_var, show="*", 
                        font=("Arial", 11), bg='#2d2d2d', fg='#ffffff', 
                        insertbackground='#ffffff', relief="sunken", bd=2,
                        width=60)
        entry.pack(fill='x')
    
    def create_text_input(self, parent, label_text, var_name, default_value):
        """创建文本输入组件"""
        # 主框架
        section_frame = tk.Frame(parent, bg='#1e1e1e')
        section_frame.pack(fill='x', pady=15)
        
        # 标签
        label = tk.Label(section_frame, text=label_text, 
                        font=("Arial", 12, "bold"), 
                        bg='#1e1e1e', fg='#ffffff',
                        anchor="w")
        label.pack(fill='x', pady=(0, 5))
        
        # 文本输入框
        setattr(self, f"{var_name}_var", tk.StringVar(value=default_value))
        entry = tk.Entry(section_frame, textvariable=getattr(self, f"{var_name}_var"), 
                        font=("Arial", 11), bg='#2d2d2d', fg='#ffffff', 
                        insertbackground='#ffffff', relief="sunken", bd=2,
                        width=60)
        entry.pack(fill='x')
    
    def browse_folder(self, var_name, title):
        """浏览文件夹"""
        folder_path = filedialog.askdirectory(title=title)
        if folder_path:
            getattr(self, f"{var_name}_var").set(folder_path)
    
    def browse_file(self, var_name, title, filetypes):
        """浏览文件"""
        file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
        if file_path:
            getattr(self, f"{var_name}_var").set(file_path)
    
    def start_processing(self):
        """开始处理PDF文件"""
        # 获取输入值
        src_folder = self.src_folder_var.get().strip()
        dst_folder = self.dst_folder_var.get().strip()
        excel_file = self.excel_file_var.get().strip()
        password = self.password_var.get().strip()
        header_text = self.header_text_var.get().strip()
        
        # 验证输入
        if not all([src_folder, dst_folder, excel_file, password]):
            messagebox.showerror("错误", "请填写所有必要信息！")
            return
        
        if not os.path.exists(src_folder):
            messagebox.showerror("错误", "源文件夹不存在！")
            return
        
        if not os.path.exists(excel_file):
            messagebox.showerror("错误", "Excel文件不存在！")
            return
        
        # 更新状态
        self.status_label.config(text="⏳ 正在处理，请稍候...", fg="#FFC107")
        self.root.update()
        
        try:
            # 开始批处理
            self.batch_processor.process_folder(src_folder, dst_folder, excel_file, password, header_text)
            
            # 处理完成
            self.status_label.config(text="✅ 处理完成！", fg="#4CAF50")
            messagebox.showinfo("完成", "PDF批处理完成！")
            
        except Exception as e:
            error_msg = f"处理过程中出现错误：{str(e)}"
            self.status_label.config(text="❌ 处理失败", fg="#F44336")
            messagebox.showerror("错误", error_msg)
    
    def run(self):
        """运行GUI"""
        self.root.mainloop()
