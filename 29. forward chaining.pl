/* Declare dynamic predicates */
:- dynamic fact/2.

/* Define the knowledge base */
fact(mammal, dog).
fact(mammal, cat).
fact(animal, dog).
fact(animal, cat).
fact(animal, bird).

/* Define the rules */
rule(fact(animal, X), fact(mammal, X)).
rule(fact(animal, X), fact(bird, X)).
rule(fact(mammal, X), fact(has_fur, X)).
rule(fact(has_fur, X), fact(mammal, X)).

/* Forward chaining algorithm */
forward_chaining :-
    findall(rule(Head, Body), rule(Head, Body), Rules),
    forward(Rules).

forward(Rules) :-
    ( apply_rules(Rules) ->
        forward(Rules)
    ;
        write('No more rules can be applied.'), nl
    ).

apply_rules([]) :-
    fail.
apply_rules([rule(Head, Body)|Rules]) :-
    ( call(Body) ->
        assertz(Head),
        write('Derived: '), write(Head), nl,
        ! % Cut to stop after the first applicable rule
    ;
        apply_rules(Rules)
    ).

/* Define a predicate to query the knowledge base */
query(Goal) :-
    ( call(Goal) ->
        write('Yes'), nl
    ;
        write('No'), nl).
