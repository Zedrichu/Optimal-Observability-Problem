from placements.GraphSearch import GraphSearch
from placements.State import State

if __name__ == "__main__":
    n = 15
    sensors = {0,1,2,3,4,5,6}
    bits = bytearray([int(i in sensors) for i in range(n)])

    placement = State(n=n, goal=7, bits=bits, g=0, parent=None)

    gs = GraphSearch(n)
    gs.search(placement)
