# 项目结构说明

```
pdf_processor/                    # 项目根目录
├── src/                         # 源代码目录
│   ├── __init__.py             # Python包初始化文件
│   ├── pdf_processor.py        # PDF处理核心功能模块
│   ├── batch_processor.py      # 批处理功能模块
│   └── gui.py                  # 图形用户界面模块
├── config/                      # 配置文件目录
│   ├── __init__.py             # Python包初始化文件
│   └── settings.py             # 程序配置文件
├── data/                        # 数据文件目录
│   └── example_data.csv        # 示例数据文件
├── output/                      # 输出文件目录（处理后的PDF存放位置）
├── main.py                     # 主程序入口
├── run.py                      # 快速启动脚本
├── requirements.txt            # 项目依赖包列表
├── README.md                   # 项目说明文档
└── PROJECT_STRUCTURE.md        # 项目结构说明（本文件）
```

## 各文件说明

### 核心功能模块 (src/)
- **pdf_processor.py**: 包含PDFProcessor类，负责单个PDF文件的页眉页脚添加和加密
- **batch_processor.py**: 包含BatchProcessor类，负责批量处理多个PDF文件
- **gui.py**: 包含PDFProcessorGUI类，提供图形用户界面

### 配置文件 (config/)
- **settings.py**: 存储程序的配置参数，如字体、页面设置等

### 数据文件 (data/)
- **example_data.csv**: 示例数据文件，展示Excel文件格式

### 主程序文件
- **main.py**: 程序主入口，启动GUI界面
- **run.py**: 快速启动脚本，确保模块路径正确

### 文档文件
- **README.md**: 详细的项目说明和使用指南
- **requirements.txt**: 项目依赖包列表
- **PROJECT_STRUCTURE.md**: 项目结构说明（本文件）

## 使用流程

1. 安装依赖: `pip install -r requirements.txt`
2. 运行程序: `python main.py` 或 `python run.py`
3. 在GUI界面中设置参数并开始处理
