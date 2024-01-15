# demo-python
## 环境
### 使用virtual env  
`python -m venv .venv`: 在.venv文件夹创建虚拟环境  
vscode: .vscode/settings.json添加`"python.defaultInterpreterPath":".venv/bin/python"`

### pip镜像
`pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/`

### 依赖
`pip install -r requirements.txt`: 安装requirements.txt的依赖
`pip freeze > requirements.txt`: 导出已安装的依赖到requirements.txt  
在安装依赖的过程中, 如果有遇到"Failed building wheel for xxxx"的错误, 可能是requirements.txt定义的版本太旧了, 可以到[pypi](https://pypi.org/search) 搜索最新的版本

#### 升级
升级pip: `pip install --upgrade pip`  
升级所有的包: `pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U`  
查看可以升级的包: `pip list --outdated`  
升级后记得再写入requirements.txt


## 执行
### 执行整个脚本文件
vscode和pycharm直接执行此文件即可
### 执行单个方法
这边需要借助单元测试,所以需要继承`unittest.TestCase`类,**并且要运行的方法名要以test开头**,
#### vscode
vscode这边是借助Python Test Explorer for Visual Studio Code这个插件来执行单测的, 它根据.vscode/settings.json的`python.testing.unittestArgs`配置项来搜索文件,
这边直接配置了'*.py',同时搜索路径使用项目根路径,子目录的文件如果需要被搜索到,**则子目录需要添加一个空的`__init__.py`文件**  
查看print输入的内容, run的话,需要打开OUTPUT(⇧+⌘+U),然后切换到Python Test Log, debug的话,则输入在DEBUG CONSOLE(⇧+⌘+Y)
#### pycharm
直接运行test方法即可

## 格式化
使用black
vscode安装:[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)  
pycharm配置参考https://black.readthedocs.io/en/stable/integrations/editors.html  
行数限制的话,在black的参数"$FilePath$"后面添加`-l 160`

