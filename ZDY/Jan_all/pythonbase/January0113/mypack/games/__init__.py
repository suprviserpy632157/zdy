# file:mypack/games/__init__.py

# 此列表会在from mypack.games import *导入时，
# 导入contra模块和supermario模块
__all__=['contra','supermario']

print("mypack.games子包被导入")