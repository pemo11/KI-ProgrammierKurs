# Einführung in Machine Learning

In den 90er Jahren sollte ein Programm geschrieben werden, dass anhand von Röntenaufnahmen erkennen soll, ob ein Patient eine Lugenentzüdung hat. Das war mit dem damaligen Stand der Technik unmöglich, das Projekt wurde schnell wieder aufgegeben.

2017 wurde an der Standford Universität in den USA ein Algorithmus vorgestellt, der genau das kann und besser als jeder Radiologe arbeitet.

Sind die Entwickler in knapp 20 Jahren so viel besser geworden? Wurden neue Programmiersprachen entwickelt, die so viel besser sind als die alten?

Weder noch, der Algorithmus basiert auf Machine Learning.

Machine Learning bedeutt, dass ein Algorithmus aus vorhandenen Daten lernt und damit in der Lage ist, das Erlernte auf unbekannte Daten anzuwenden.

Bei der traditionellen Programmierung müssen alle Fälle und Eventualitäten durch Programmbefehle abgebildet werden.

Programme werden dadurch umfangreich und insgesamt unflexibel, da sie für jede Änderung bei de Art und Weise wie sie die neuen Daten erkennen sollen angepasst werden müssen.

Die zur Zeit wichtigste Art des Lernens heißt Reinforcement Learning (ein Begriff aus der Psychologie). Zu Deutsch "Verstärkendes Lernen".

Ein Computerprogramm soll ein Videospiel erfolgreich spielen, kennt aber die Regel nicht.

Anstatt ihm in die Regeln einzuprogrammieren, soll das Programm sie selber herausfinden.

Und wie soll das gehen?

Ganz einfach, in dem das Programm willkürlich Spielzüge ausprobiert und für jeden Zug eine Information darüber erhält, ob der Zug erfolgreich war oder nicht. Es gibt eine Belohnung, die davon abhängt, wie gut der Zug dafür geeignet war, das Ziel zu erreichen.

Das Spiel muss kein komplexes Ziel sein, es kann darin bestehen, einen Ball in ein Tor zu befördern.

In dem das Programm sehr viele Befehle ausführt, kommt es langsam dahinter, welche Aneinanderreihung von Befehlen dem Ziel näher kamen und welche nicht. Irgendwann entsteht dann eine Befehlsfolge, die zum Ziel führt und das Programm hat die Regeln des Spiels "verstanden", in dem es durch Anwendung er der erlernten Spielzüge das Spiel und eventuell jede Spielrunde gewinnt.

Das prominenteste Beispiel ist sicherlich AlfaGo, das in einem aufseheneregenden Turnier gegen den besten Go-Spieler der Welt Lee Sedol von 5 Spielen im Jahr 2016 vier Spiele und damit das Turnier gewonnen hatte. AlfaGo verwendete dafür unter anderem verstärkendes Lernen.

Ein sehr nettes und anschauliches Beispiel sind die "Abenteuer von Albert". Albert ist eine Spielfigur von AI Warehouse, die einfache Fähigkeiten wie 

