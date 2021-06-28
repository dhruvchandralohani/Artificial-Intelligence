sumlist([], 0).
sumlist([First|Rest], Sum):- sumlist(Rest, SumRest), Sum is First + SumRest.
