# 冒泡排序
def bubble(heights):
    # 外层循环:走访次数
    for i in range(len(heights)-1):
        # 内层循环:每次走访数据时,相邻数据对比次数
        for j in range(len(heights) - i - 1):
            # 要求从低到高
            if heights[j] > heights[j + 1]:
                heights[j],heights[j+1] = heights[j+1],heights[j]
    
    # 走访数据次数
    print('走访次数:',i+1)
            
if __name__ == "__main__":
    heights = [160, 180, 176, 154, 124, 134, 184, 155, 158, 110]
    print("排序前",heights)
    bubble(heights)
    print("排序后",heights)