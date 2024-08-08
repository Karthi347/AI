/* Define the knowledge base */
fact(mammal, dog).
fact(mammal, cat).
fact(animal, dog).
fact(animal, cat).
fact(animal, bird).

rule(derived(animal, X), [fact(mammal, X)]).
rule(derived(animal, X), [fact(bird, X)]).
rule(derived(mammal, X), [fact(has_fur, X)]).
rule(derived(has_fur, X), [fact(mammal, X)]).

/* Define the backward chaining algorithm */
backward_chaining(Goal) :-
    prove(Goal, []).

prove(true, _) :- !.
prove((A, B), Proof) :- !,
    prove(A, Proof),
    prove(B, Proof).
prove(Goal, Proof) :-
    member(Goal, Proof), !. % Prevent infinite loops
prove(fact(Predicate, Arg), _) :-
    fact(Predicate, Arg), !.
prove(Goal, Proof) :-
    rule(Goal, Subgoals),
    prove_all(Subgoals, [Goal|Proof]).

prove_all([], _) :- !.
prove_all([Subgoal|Subgoals], Proof) :-
    prove(Subgoal, Proof),
    prove_all(Subgoals, Proof).

/* Define a predicate to query the knowledge base */
query(Goal) :-
    (backward_chaining(Goal) ->
        write('Yes'), nl
    ;
        write('No'), nl).
