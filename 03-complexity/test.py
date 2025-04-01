import sys
class Rectangle:
    def __init__(self,a:int,b:int):
        self.a = a
        self.b = b

    def find(self,x:int,y:int) ->bool:
        if(x==20 and y==20):
            return True
        else:
            return False


def load_data(path:str) ->list[Rectangle]:
    list_r:list[Rectangle]  = []
    with open(path,"r",encoding="UTF-8") as f:
        for line in f:
            data = line.strip().split("x")
            rect = Rectangle(int(data[0]),int(data[1]))
            list_r.append(rect)
    return list_r

def main():
    arguments = sys.argv[1]
    list = load_data(arguments)
    index = 0
    for i,value in enumerate(list):
        if(value.find(value.a,value.b)):
            print(i)
        index+=1

if __name__ == "__main__":
    main()



