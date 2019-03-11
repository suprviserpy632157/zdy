# 1.公鸡５文钱一只，母鸡３文钱一只，小鸡３只１文钱，
# 用１００文买１００只鸡其中公鸡，小鸡，母鸡都必须要有，
# 问公鸡，母鸡，小鸡要买多少只刚好凑足１００文钱
def buy_chicken():
    for cock in range(5,101,5):
        for hen in range(3,101-cock,3):
            for chick in range(1,101-cock-hen):
                if 5+hen//3+chick*3==100 and \
                cock +hen+chick==100:
                    print("公鸡有%d只\母鸡有%d只\小鸡有%d只"%(cock//5,hen//3,chick*3))
buy_chicken()
    