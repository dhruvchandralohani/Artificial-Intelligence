secretsociety(freemasons).
secretsociety(illuminati).
secretsociety(theskullandbones).
secretsociety(therosicrucians).
secretsociety(thenineunknown).
europe(freemasons).
europe(illuminati).
america(theskullandbones).
europe(therosicrucians).
india(thenineunknown).
active(freemasons).
notActive(illuminati).
notActive(theskullandbones).
notActive(therosicrucians).
notActive(thenineunknown).

society(X):- secretsociety(X).
will_die(X):- secretsociety(X), active(X).
