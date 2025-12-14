from placements.GraphSearch import GraphSearch
from placements.State import State
from Z3Executor import Z3Executor
from builders.POMDPSpec import POMDPAdapter
from builders.ssp import LineTPMC

if __name__ == "__main__":
    B = 6
    goal = 7
    n = 15

    obs = [1 if i<B else -1 if i==goal else 0 for i in range(n)]
    placement = State(n=n, goal=7, obs=obs, g=0, parent=None)
    threshold = "<=Q(9,2)"

    tpmc = LineTPMC(budget=B, goal=goal,length=n)
    solver = Z3Executor(tpmc.ctx, verbose=True)
    adapter = POMDPAdapter(tpmc)
    solver.prepare_constraints(adapter, threshold)

    gs = GraphSearch(n, adapter, solver)
    solution = gs.search(placement)
    if solution is not None:
        print(f"Solution is SSP instance with obs. function={solution.obs}")
