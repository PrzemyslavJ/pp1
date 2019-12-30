import QuadraticEquation
wsp = QuadraticEquation.czytajWspolczynniki()
delta = QuadraticEquation.obliczDelte(wsp)
Pierw = QuadraticEquation.wyznaczPierwiastki(delta,wsp)
QuadraticEquation.wyswietlpierwiastki(Pierw)
