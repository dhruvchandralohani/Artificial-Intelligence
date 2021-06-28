dlt(1, [_|T], T).
dlt(P, [X|Y], [X|R]):- P1 is P - 1, dlt(P1, Y, R).
