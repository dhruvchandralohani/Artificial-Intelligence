fact(1, 1).
fact(X, R):- X1 is X - 1, fact(X1, R1), R is X * R1.
