# Grundlagen ML

ML steht für maschinenelles Lernen oder auch "Machine Learning".

Die Maschine lernt also, doch was lernt sie?

Eine große Verständnishürde kann es sein, dass der Begriff lernen eine sehr eng umrissene Bedeutung besitzt.

Ein Mensch lernt, in dem er/sie/es z.B. einigen Seiten in einem Lehrbuch liest und dabei versucht, sich die wichtigsten Fakten einzuprägen und vor allem auch, dass gelesene zu verstehen.

Dieser Lernprozess spielt sich in unserem Gehirn ab, ist enorm komplex und von Mensch zu Mensch unterschiedlich. Die einen müssen einen Text nur lesen, um seinen Inhalt zu behalten, die anderen können sich auch bei wiederholtem Lesen nur an einige Fakten erinnern. Die einen haben eine schnelle Auffassungsgabe, die anderen weniger. Die einen fangen rechtzeitig anderen, die anderen warten bis zum letzten Moment usw.

Das hat alles hat nichts mit ML zu tun.

Bei ML hat der Begriff Lernen eine engumrissene Bedeutung.

Lernen bei ML ist eien Prozess, durch den ein Modell aus Daten Muster und Strukturen erkennt, um Vorhersagen zu treffen oder Entscheidungen zu treffen, ohne dafür explizit programmiert zu sein.

Dass für erfahrene Entwickler eventuell ein "Kulturschock". Ein Programm erzeugt ein Ergebnis, ohne dass die dafür erforderlichen Rechenschritte explizit programmiert wurden.

Wir haben es hier aber nicht mit einer klassischen Blackbox zu tun, die irgendetwas Geheimnisvolles macht.

Das Gegenteil ist der Fall. Die verwendeteten Algorithmen sind Standardalgorithmen aus den Bereichen Statistik und Mathematik, alles ist Open Source. Es gibt keine Blackbox, die irgendetwas macht.

Es ist allerdings so, dass es bei bestimmten Lerntypen auch für die Entwickler der Anwendung nicht nachvollziehbar ist, wie die KI auf ein Ergebnis kommt.

Das kann in der Praxis ernste Konsequenzen haben. Eine Bank lernt einen Kreditantrag ab, ohne dass dies im Detail begründet werden kann. Einem Reisenden wird die Einreise verweigert oder muss sich einer ausführlichen Kontrolle unterziehen. Ein Lehrerin wird entlassen, da sie im Rahmen einer automatisierten Bewertung nicht die erforderliche Mindespunktzahl erreicht hat. Diese Liste ließe sich noch fortsetzen.

Aber darum soll es im Folgenden natürlich nicht gehen. Es soll nur deutlich werden, dass es unterschiedliche Lernalgorithemn gibt. Während das Ergebnis einer linearen Regression oder Klassifikation auf relativ einfachen mathematischen Formeln basiert, die sich immer nachrechen lassen, ist das beim "Deep Learning" nicht der Fall. 

Auch dazu später noch mehr.

Halten wir fest:

Der Lernprozess bei ML basiert auf bekannten Algorithmen, die je nach Art der Aufgabe und des verfügbaren Datensatzes variieren können.


### Die Rolle des Modells

Der wichtigste Begriff beim ML ist der Begriff Modell.

Auch dieser Begriff hat in der Programmierung sowie in der Umgangssprache eine andere Bedeutung als bei ML.

Bei ML ist ein Modell ist ein mathematisches oder statistisches Konstrukt, das durch den Vorgang des Trainierens eine bestimmte Beziehung zwischen den Eingaben (Daten) und den Ausgaben (Ergebnissen) erlernt hat. Nach dem Training wird das Modell dazu benutzt, auf der Grundlage von Eingabedaten die gewünschte Ausgabe zu erhalten.

Bei ML.Net ist das Modell am Ende ein Zip-Archiv.

Bei sehr einfachen Modellen ist das, was als "mathematisches Konstrukt" bezeichnet wird, eine einfache linerare Regression. Durch das Trainieren mit Trainingsdaten wurde eine optimale Linie gefunden, die durch das Anwenden auf Testdaten bewertet wurde. Ist das Ergebnis zufriedenstellend, kann das Modell bereitgestellt und im Rahmen einer Anwendung benutzt werden.

Bei aller Theorie und den vielen neuen Begriffen darf nicht vergessen werden, dass am Ende eine Anwendung herauskommt, die für ihre Anwender einen spürbaren Mehrwert bieten soll.

Ein Model basiert auf einer einfachen mathematischen Funktion:

y = f(x;θ)

x = Eingabedaten
θ = Parameter des Modells, die während des Trainings erlernt werden
y = Ausgabe (? gibt es die wirklich)

f = Die durch den gewählten Algorithmus definierte Funktion (z. B. lineare Regression, Entscheidungsbaum, neuronales Netz usw.)


xxx

Es gibt verschiedene Arten des ML:

### Überwachtes Lernen (supervised learning)

Ein Model wird mit gezeichneten Daten (Labels) trainiert.

Das Ziel ist es, eine Funktion f(x) zu "erlernen", die Eingabe x den gewünschten Ausgaben y zuordnet.

Beispiele für Methoden, die auf überwachtem Lernen basieren, sind:

- Klassifikation (z.B. Spamfilter)
- Regression (Vorhersage von Preisen)
  
## Nicht überwachtes Lernen (Unsupervised learning)

Bei dieser Varianten gibt es kein Model, das trainiert werden kann, da die Daten nicht gekennzeichnet sind.

Da es keine Labels gibt, versucht das Modell, Muster oder Strukturen in den Daten zu entdecken.

Das Ziel ist es daher, Muster in den Daten zu erkennen, nach denen eine Gruppierung möglich ist.

Beispiele für Methoden, die auf unüberwachten Lernen basieren, sind:

xxx

### Verstärktes Lernen (Reinforcement learning)

Dies ist die leistungsstärkste Variante.

Ein Agent lernt durch Interaktionen mit einer Umgebung, wie er durch Belohnungen optimale Aktionen auswählt.

Denkt noch einmal an die animierte Figur Albert, die versucht laufen zu lernen und am Ende nach unzähligen Versuchen auch erfolgreich ist.

[https://www.youtube.com/watch?v=xk8wHY1AFpI](https://www.youtube.com/watch?v=xk8wHY1AFpI)

