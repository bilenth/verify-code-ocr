#### 直接启动
cd src
pip install -r requirements.txt
python app.py

#### 没有.spec文件时要先生成这个文件
docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux "pyinstaller app.py"

#### 打包成不同系统的版本
docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux "pyinstaller --onefile --noconsole app.py"
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows "pyinstaller --onefile --noconsole app.py"