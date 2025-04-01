from collections import defaultdict
import os
import sys



class Record():
    time:int
    id_cust:int
    ckpt:str

    def __init__(self,time:int ,id_cust: int,ckpt:str) -> None:
        self.time = time
        self.id_cust = id_cust
        self.ckpt = ckpt



def load_data(data_path:str ,city:str ,shop:str, day="1-Mon") -> dict[str, list[Record]]:

    path = f"{data_path}/{city}/{day}/{shop}.txt"
    city_data: dict[str, list[Record]] = defaultdict(lambda: list())
    with open(path,encoding="utf-8") as f:
        f.readline()
        for line in f:
            line.strip()
            data_list = line.split(";")
            record = Record(int(data_list[0]),int(data_list[2]),data_list[1])
            city_data[record.ckpt].append(record)

    print("loading", city)

    return city_data


def get_passed_set(data : dict[str, list[Record]],key_words:set[str]) -> set[int]:


    customers : set[int] = set()
    for k,v in data.items():
        checkpoint_name = k[: k.find("_")]
        if checkpoint_name in key_words:
            for record in v: 
                customers.add(record.id_cust)
    return customers
            

def filter_data_time(data :dict[str, list[Record]], cond_time:int) -> dict[str, list[Record]]:
    ret: dict[str, list[Record]] = defaultdict(lambda: list())
    for k,v in data.items():
        ret[k] = [record for record in v if record.time < cond_time]

    return ret
         
def get_q_size(data :dict[str, list[Record]], seconds:int) -> int:   
    queue : set[int] = set()   
    data = filter_data_time(data, seconds)
    set_1 = get_passed_set(data,{"meat","frui","vege"})
    set_2 = get_passed_set(data,{"final-crs"})
    return len(set_1-set_2)
    

def histogram(data :dict[str, list[Record]]):
    pass

def main(data_dir: str):
    
    data = load_data(data_dir,"Plzeň","shop_a")
    print(len(data["final-crs_1"]))
    if data is not None:
        q_size = get_q_size(data,15*3600)
        print(q_size)

if __name__ == "__main__":
    datadir = sys.argv[1]
    main(datadir)
