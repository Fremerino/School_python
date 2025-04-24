
import json
from queue import PriorityQueue

import adthelpers


class Graph:
    def __init__(self) -> None:
        self.edges: dict[int, list[tuple[float, int]]] = {}

    def add_edge(self, src: int, dst: int, weight: float = 0) -> None:
        if  src not in self.edges:
            self.edges[src] = []
        self.edges[src].append((weight,dst))
        if dst not in self.edges:
            self.edges[dst] = []
        self.edges[dst].append((weight,src))
       


def load_graph(filename: str) -> Graph:
    graph = Graph()
    with open(filename) as f:
        graph_json = json.load(f)
        for edge in graph_json["links"]:
            graph.add_edge(edge["source"],edge["target"],edge["weight"])


    return graph

# strom, vyuzivame hrany a node pro to aby jsme nasli nejlepsi kostru grafu
def spanning_tree(graph: Graph) -> None:
    closed: set[int] = set()
    sp_tree: list[tuple[int, int]] = []
    queue: PriorityQueue[tuple[float,tuple[int,int]]] = PriorityQueue()

    painter = adthelpers.painter.Painter(
        graph,
        visible=queue,
        closed=closed,
        color_edges=sp_tree,
    )
    painter.draw_graph()
    queue.put((0,(-1,0)))
    while not queue.empty():
        weight, edge = queue.get()
        prev_node, current_node = edge
        if current_node in closed:
            continue
        closed.add(current_node)
        if prev_node >=0:
            sp_tree.append(edge)
        sp_tree.append(edge)
        for next_weight, next_node in graph.edges[current_node]:
            queue.put((next_weight,(current_node,next_node)))
            painter.draw_graph(current_node)
    return None
 


def main() -> None:
    graph = load_graph("data/graph_grid_s6.json")

    painter = adthelpers.painter.Painter(
        graph,
        # colors=("red", "blue", "yellow", "grey") # pokud by byl problém s barvami je možné je změnit
    )
    painter.draw_graph()

    # debug to see progress...
    spanning_tree(graph)

    # don't close before user acknowledges diagrams
    input("Press enter to exit program...")


if __name__ == "__main__":
    main()

