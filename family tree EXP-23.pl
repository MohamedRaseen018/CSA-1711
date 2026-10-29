% Facts: Parent relationships
parent(john, peter).
parent(john, mary).
parent(peter, david).
parent(peter, lisa).
parent(mary, james).
parent(mary, anna).

% Facts: Gender
male(john).
male(peter).
male(david).
male(james).

female(mary).
female(lisa).
female(anna).

% Rule: Father
father(X, Y) :-
    parent(X, Y),
    male(X).

% Rule: Mother
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Rule: Sibling
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Rule: Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Rule: Brother
brother(X, Y) :-
    sibling(X, Y),
    male(X).

% Rule: Sister
sister(X, Y) :-
    sibling(X, Y),
    female(X).
