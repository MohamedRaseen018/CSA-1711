% Monkey and Banana Problem

% Initial state:
% Monkey is at the door, box is at the window,
% and banana is hanging in the middle.

% Move monkey from one place to another
move(state(P, B, on_floor, has_not), 
     walk(P, Q), 
     state(Q, B, on_floor, has_not)).

% Monkey pushes the box
move(state(P, P, on_floor, has_not), 
     push(P, Q), 
     state(Q, Q, on_floor, has_not)).

% Monkey climbs onto the box
move(state(P, P, on_floor, has_not), 
     climb, 
     state(P, P, on_box, has_not)).

% Monkey grasps the banana
move(state(middle, middle, on_box, has_not), 
     grasp, 
     state(middle, middle, on_box, has)).

% Goal state: Monkey has the banana
goal(state(_, _, _, has)).

% Solve the problem
solve(State, []) :-
    goal(State).

solve(State, [Action | Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).
