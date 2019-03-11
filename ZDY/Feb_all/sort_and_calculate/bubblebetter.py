# 冒泡排序有序的情况
def bubble(heights):
    # 外层循环:走访次数
    for i in range(len(heights)-1):

        # 设置数据交换的标识
        flag = False

        # 内层循环:每次走访数据时,相邻数据对比次数
        for j in range(len(heights) - i - 1):
            # 要求从低到高
            if heights[j] > heights[j + 1]:
                heights[j],heights[j+1] = heights[j+1],heights[j]

                # 更改数据交换标识
                flag = True

        # 若未发生数据交换,则说明后续数据均有序,跳出数据走访
        if flag == False:
            break

    # 走访数据次数
    print('走访次数:',i+1)
            
if __name__ == "__main__":
    heights = [300,110, 124, 134, 154, 155, 158, 160, 176, 180, 184]
    print("排序前",heights)
    bubble(heights)
    print("排序后",heights)