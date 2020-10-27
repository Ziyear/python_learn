# 在当前路径创建 setup.py 文件
# -- bao
#    setup.py
#    infodisplay.py
#    -- TestMsg
#       sendmsg.py
#       receive.py

# 设置模块信息
# from distutils.core import setup
# setup(name="Ziyear", version="1.0", description="Ziyear's model", author="Ziyear",
#       py_modules=['TestMsg.receive', 'TestMsg.sendmsg'])

# >python setup.py build
# >python setup.py sdist

# 解压 Ziyear-1.0.tar.gz