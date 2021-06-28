maxlist([X], X):- !.
maxlist([X, Y|Rest], Max):- maxlist([Y|Rest], MaxRest), max(X, MaxRest, Max), !.
max(X, Y, X):- X >= Y.
max(X, Y, Y):- X < Y.
