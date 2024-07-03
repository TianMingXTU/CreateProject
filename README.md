# 使用chatGPT等大模型开发者的便利

## 使用说明

### 安装依赖
确保已安装以下Python库：
- PyQt5
- PyYAML

可以使用以下命令安装所需库：
```bash
pip install PyQt5 PyYAML
```

### 运行程序
运行以下命令启动应用程序：
```bash
python main.py
```

### 输入目录结构
在文本框中输入目录结构，格式如下：
```
Project/
├── main.py
├── requirements.txt
├── src/
│   ├── module1.py
│   ├── module2.py
│   └── utils/
│       ├── helper.py
│       └── logger.py
├── tests/
│   ├── test_module1.py
│   ├── test_module2.py
│   └── test_utils/
│       ├── test_helper.py
│       └── test_logger.py
├── docs/
│   ├── index.md
│   └── installation.md
└── README.md
```

### 导入结构
点击“导入结构”按钮，从JSON或YAML文件中加载目录结构。

### 导出结构
点击“导出结构”按钮，将当前目录结构保存为JSON或YAML文件。

### 选择保存目录
点击“选择目录保存”按钮，选择保存目录，程序会在该目录下创建输入的目录结构，并显示创建进度。

### 进度显示
创建目录结构时，进度条会显示创建进度。

### 作者碎碎念
点击“作者碎碎念”按钮，查看作者的备注信息。

## 进阶功能

### 高级配置选项
在创建目录和文件时，支持设置文件内容、权限和所有者。

### 支持多种输入格式
除了文本格式，还支持导入和导出JSON和YAML格式的目录结构。

## 示例

### 示例1: 文本输入
```
Project/
├── main.py
├── requirements.txt
├── src/
│   ├── module1.py
│   ├── module2.py
│   └── utils/
│       ├── helper.py
│       └── logger.py
├── tests/
│   ├── test_module1.py
│   ├── test_module2.py
│   └── test_utils/
│       ├── test_helper.py
│       └── test_logger.py
├── docs/
│   ├── index.md
│   └── installation.md
└── README.md
```

### 示例2: JSON 输入
```json
{
    "Project": {
        "main.py": "",
        "requirements.txt": "",
        "src": {
            "module1.py": "",
            "module2.py": "",
            "utils": {
                "helper.py": "",
                "logger.py": ""
            }
        },
        "tests": {
            "test_module1.py": "",
            "test_module2.py": "",
            "test_utils": {
                "test_helper.py": "",
                "test_logger.py": ""
            }
        },
        "docs": {
            "index.md": "",
            "installation.md": ""
        },
        "README.md": ""
    }
}
```

### 示例3: YAML 输入
```yaml
Project:
  main.py: ""
  requirements.txt: ""
  src:
    module1.py: ""
    module2.py: ""
    utils:
      helper.py: ""
      logger.py: ""
  tests:
    test_module1.py: ""
    test_module2.py: ""
    test_utils:
      test_helper.py: ""
      test_logger.py: ""
  docs:
    index.md: ""
    installation.md: ""
  README.md: ""
```

## 开发者备注
该工具旨在帮助开发者快速搭建项目目录结构。如有任何问题或反馈，请联系作者。祝您编码愉快！

## 许可证
MIT 许可证

## 贡献
欢迎提交问题和功能请求。如需贡献，请提交Pull Request。
