from dataclasses import dataclass
import random
import timeit
from typing import Callable
import time
import plotly.graph_objects as go
#import plotly.express as px  

COLLECTION_SIZE = 100000
N_TESTS = 100  # Number of test runs


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def test_operation_in(collection: list|set) -> bool:
    rand = random.randint(0,len(collection))
    return -1 in collection
    

def test_collection(our_collection: list|set ,test_function: Callable) -> float:
    n = 1
    elapsed_in = 0.0
    for _ in range(n):
        start_time = time.time()
        res = test_function(our_collection)
        end_time = time.time()
        elapsed_in += end_time-start_time
    return elapsed_in

                                                                                           
    

def main():
    times = []
    set_times = []
    n = 1000
    l = []
    for i in range(1000):
        l.append(random.randint(0,1000))
        times.append(test_collection(l,test_operation_in))
        set_times.append(test_collection(set(l),test_operation_in))
    plot_experiments({"List":times,"set":set_times},list(range(1000)))


def plot_experiments(experiments: dict[str, list[float]], x_axis: list[int]) -> None:
    fig = go.Figure()
	
    for method, timings in experiments.items():
        fig.add_trace(go.Scatter(
            x=x_axis,
            y=timings,
            name=method,
        ))
		
    fig.update_layout(
        yaxis={
            "ticksuffix": "s",
            "title": "Time (seconds)",
        }
    )
	
    fig.show()




if __name__ == "__main__":
    experiments = {
    "in_set": [1.4, 1.3, 2.0, 1.0, 2.0],
    "in_list": [1.3, 1.4, 1.2, 1.5, 1.9]
    }
    x_axis = [0, 1, 2, 3, 4]

    main()
   

