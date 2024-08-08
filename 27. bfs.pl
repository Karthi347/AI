% Define the graph using edges
edge(a, b, 1).
edge(a, c, 2).
edge(b, d, 5).
edge(b, e, 4).
edge(c, f, 6).
edge(c, g, 3).
edge(g, d, 1).

% Define the heuristic function (h(n)) for each node
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 0).
heuristic(e, 1).
heuristic(f, 4).
heuristic(g, 2).

% Define the Best First Search algorithm
best_first_search(Start, Goal, Path, Cost) :-
    heuristic(Start, H),
    bfs([H-Start-0], Goal, [], Path, Cost).

% BFS implementation
bfs([_-Goal-Cost|_], Goal, _, [Goal], Cost).

bfs([_-Node-Cost|Rest], Goal, Visited, [Node|Path], TotalCost) :-
    findall(NewH-Next-NewCost,
            (edge(Node, Next, StepCost),
             \+ member(Next, Visited),
             heuristic(Next, H),
             NewCost is Cost + StepCost,
             NewH is H + NewCost),
            Children),
    append(Rest, Children, NewQueue),
    keysort(NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, [Node|Visited], Path, TotalCost).
