% Facts: Birds
bird(sparrow).
bird(parrot).
bird(pigeon).
bird(ostrich).
bird(penguin).
bird(eagle).

% Facts: Birds that can fly
can_fly(sparrow).
can_fly(parrot).
can_fly(pigeon).
can_fly(eagle).

% Rule: Birds that cannot fly
cannot_fly(Bird) :-
    bird(Bird),
    \+ can_fly(Bird).
