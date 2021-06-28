fib(1, 0):-!.
fib(2, 1):-!.
fib(3, 1):-!.
fib(X, R):- X1 is X - 1, fib(X1, R1), X2 is X - 2, fib(X2, R2), R is R1 + R2. 
