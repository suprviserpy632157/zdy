# file:mypack/games/contra.py
def play():
    print("正在玩魂斗罗!!!")
def gameover():
    print("魂斗罗游戏结束!!!")
    #调用上一层文件夹里的menu.py里的shoe_menu函数   
    # # #用绝对导入的方式
    # from mypack.menu import show_menu
    # #调用
    # show_menu() 
    # #用相对导入方式
    # from ..menu import show_menu
    # show_menu()
    # 在此处调用ｔａｎｋｓ．ｐｙ里的ｐｌａｙ（）
    # #1
    # import mypack.games.tanks as t
    # t.play()
    # #2
    # from mypack.games.tanks import play
    # play()
    # #3.
    # from .tanks import play
    # play()
print("魂斗罗模块被加载!!!")