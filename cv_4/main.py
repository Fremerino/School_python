
from collections import deque 
import random


class NamedQueue:
    def __init__(self, name:str):
        self.name:str = name
        self.fronta:deque = deque([])


class ProcessingNode:
    def __init__(self,name: str,period: int,source: NamedQueue,destination: NamedQueue,sigma: float = 0.1,):
        self.name = name 
        self.period = period 
        self.source = source 
        self.destination = destination
        self.sigma = sigma
        self.timer = self.next_occur_in()
        
        
    def perform(self) -> None:
        if len(self.source.fronta)>0:
          
            self.destination.fronta.append(self.source.fronta.popleft())

    def next_occur_in(self) -> int:
        return int(random.gauss(self.period, self.sigma))
    
    def tick(self) -> None:
        if self.timer>0:
            self.timer -=1
        else: 
            self.timer = self.next_occur_in()
            self.perform()

class Observer:
    def __init__(self, list_to_observe: list[NamedQueue]):
        self.lists = list_to_observe
    def show(self):
        return "->".join([f"{queue.name} {len(queue.fronta)}"for queue in self.lists])

def main():
    fronta_ulice = NamedQueue("Ulice")
    fronta_shop = NamedQueue("Shop")
    fronta_z = NamedQueue("zelenina")
    fronta_p = NamedQueue("pokladna")
    fronta_gone = NamedQueue("Gone")


    server_1 = ProcessingNode("server",10,fronta_z,fronta_p)
    server_2 = ProcessingNode("server",10,fronta_p,fronta_gone)
    server_3 = ProcessingNode("server",10,fronta_ulice,fronta_shop)
    server_4 = ProcessingNode("server",10,fronta_shop,fronta_z)
    observer = Observer([fronta_ulice,fronta_shop,fronta_z,fronta_p,fronta_gone])
    for i in range(10000):
        fronta_ulice.fronta.append(i)
    for second in range(24*60*60):
        server_1.tick()
        server_2.tick()
        server_3.tick()
        server_4.tick()
        if second%60==0:
            print(observer.show())


if __name__ == '__main__':
    main()
