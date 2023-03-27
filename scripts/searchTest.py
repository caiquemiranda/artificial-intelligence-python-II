from searchGeneric import Searcher, AStarSearcher
from searchBranchAndBound import DF_branch_and_bound
from searchMPP import SearcherMPP

DF_branch_and_bound.max_display_level = 1
Searcher.max_display_level = 1

def run(problem,name):
    print("\n\n*******",name)

    print("\nA*:")
    asearcher = AStarSearcher(problem)
    print("Path found:", asearcher.search(), " cost=",asearcher.solution.cost)
    print("there are", asearcher.frontier.count(asearcher.solution.cost),
    "elements remaining on the queue with f-value=", asearcher.solution.cost)

    print("\nA* with MPP:"),
    msearcher = SearcherMPP(problem)
    print("Path found:", msearcher.search(), " cost=",msearcher.solution.cost)
    print("there are", msearcher.frontier.count(msearcher.solution.cost),
    "elements remaining on the queue with f-value=", msearcher.solution.cost)

    bound = asearcher.solution.cost+0.01
    print("\nBranch and bound (with too-good initial bound of", bound, ")")
    tbb = DF_branch_and_bound(problem, bound)
    print("Path found:", tbb.search(), " cost=", tbb.solution.cost)
    print("Rerunning B&B")
    print("Path found:", tbb.search())

    bbound = asearcher.solution.cost*2+10
    print("\nBranch and bound (with not-very-good initial bound of", bbound, ")")
    tbb2 = DF_branch_and_bound(problem, bbound)
    print("Path found:",tbb2.search(), " cost=", tbb2.solution.cost)
    print("Rerunning B&B")
    print("Path found:", tbb2.search())

    print("\nDepth-first search: (Use ˆC if it goes on forever)")
    tsearcher = Searcher(problem)
    print("Path found:", tsearcher.search(), " cost=", tsearcher.solution.cost)


import searchProblem
from searchTest import run

if __name__ == "__main__":
    run(searchProblem.problem1, "Problem 1")