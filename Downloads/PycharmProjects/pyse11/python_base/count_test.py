'''
python引包顺序
1.在当前目录下面找count
2.python安装目录下   import count
3.环境变量path
4.报错（importError not find "count" module
5.model添加__inti__.py
6.软添加path
import sys
将model目录添加到系统环境path下
sys.path.append("./model")   相对路径
'''
import sys
'''将model目录添加到系统环境path下'''
sys.path.append("./model")  # 相对路径

from model.count_bb import add_bb

c = add_bb()

print(c)
