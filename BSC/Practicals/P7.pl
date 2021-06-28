dlt(1, [_|T], T).
dlt(P, [X|Y], [X|R]):- P1 is P - 1, dlt(P1, Y, R).
dltBA(P, L, R):- P1 is P - 1, dlt(P1, L, R1), dlt(P, R1, R).
