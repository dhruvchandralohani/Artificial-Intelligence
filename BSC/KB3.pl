happy(vincent).
listensToMusic(butch).
playsAirGuitar(vincent) :- listensToMusic(vincent) , happy(vincent).
playsAirGuitar(butch) :- happy(butch).
playsAitGuitar(butch) :- listensToMusic(butch).
