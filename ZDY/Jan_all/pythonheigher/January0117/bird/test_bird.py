from eagle import *
from ostrich import *

if __name__=="__main__":
    ea=Eagle("eagle",5,"打扑克")
    ea.eat()
    ea.fly()
    ea.reproduction()
    print("-----------------")
    os=Ostrich("ostrich",8,"打麻将")
    os.eat()
    os.fly()
    os.reproduction()