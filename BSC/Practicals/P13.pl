evenlength([]).
evenlength([First|Rest]):- oddlength(Rest).
oddlength([_]).
oddlength([First|Rest]):- evenlength(Rest).
