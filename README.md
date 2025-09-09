# PDF批处理工具

一个简单易用的PDF批处理工具，可以批量添加页眉页脚、加密PDF文件。

## 功能特点

- 📄 批量处理PDF文件
- 📝 自动添加页眉页脚
- 🔒 PDF文件加密
- 📊 支持Excel文件读取稿件信息
- 🖥️ 简单易用的图形界面
- 📋 详细的处理日志

## 项目结构

```
pdf_processor/
├── src/                    # 源代码目录
│   ├── pdf_processor.py   # PDF处理核心功能
│   ├── batch_processor.py # 批处理功能
│   └── gui.py             # 图形界面
├── config/                # 配置文件
│   └── settings.py        # 程序设置
├── data/                  # 数据文件目录
│   └── example_data.xlsx  # 示例Excel文件
├── output/                # 输出文件目录
├── STSONG.TTF            # 中文字体文件（必需）
├── main.py               # 主程序入口
├── run.py                # 快速启动脚本
├── requirements.txt      # 依赖包列表
└── README.md            # 项目说明
```

## 环境要求

- Python 3.11
- 推荐使用conda环境：`conda activate pdf`

## 安装和使用

### 1. 激活环境

```bash
conda activate pdf
```

### 2. 进入项目目录

```bash
cd pdf_processor
```

### 3. 安装依赖（如果尚未安装）

```bash
pip install -r requirements.txt
```

### 4. 准备文件

- 将要处理的PDF文件放在一个文件夹中
- 准备Excel文件，包含稿件编号和研究方向信息
- 确保 `STSONG.TTF` 字体文件在 `pdf_processor` 目录下

### 5. 运行程序

```bash
python main.py
```

或者使用快速启动脚本：

```bash
python run.py
```

### 6. 使用界面

1. 选择包含PDF文件的源文件夹
2. 选择处理后文件的保存位置
3. 选择包含稿件信息的Excel文件
4. 输入PDF加密密码
5. 点击"开始处理"

## Excel文件格式

Excel文件应包含两列：
- 第一列：稿件编号
- 第二列：研究方向

示例：
| 稿件编号 | 研究方向 |
|---------|---------|
| R2020024 | 企业管理 |
| R2020025 | 市场营销 |

## 注意事项

1. 确保PDF文件名格式为：`稿件编号_其他信息.pdf`
2. 程序会自动覆盖原PDF的页眉页脚区域
3. 处理后的PDF文件会被加密
4. 如有处理失败的文件，会生成 `error_log.txt` 文件
5. 字体文件 `STSONG.TTF` 必须放在 `pdf_processor` 目录下

## 技术栈

- Python 3.11
- PyPDF2 - PDF文件处理
- ReportLab - PDF生成和编辑
- Pandas - Excel文件处理
- Tkinter - 图形界面

## 作者

Logan - 2022
