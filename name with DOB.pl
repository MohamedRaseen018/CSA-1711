
% Database: Name and Date of Birth
dob(rahul, '2003-05-12').
dob(priya, '2004-08-20').
dob(amit, '2002-11-15').
dob(neha, '2003-02-10').
dob(arun, '2004-01-25').

find_dob(Name, DOB) :-
    dob(Name, DOB).
