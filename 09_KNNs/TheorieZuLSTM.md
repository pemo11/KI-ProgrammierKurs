# KI für alle
# Der große Programmierkurs für alle, die KI an Beispielen lernen wollen

## Mit KNNs Wortvorhersagen machen

Ich gebe einen Satz vor und das "Programm" gibt mir ein Wort zurück, das sehr wahrscheinlich passt.

Der Klassiker. Auf ein "Heute ist ein" könnte "schöner" oder "schlechter" folgen. 

Mit Hilfe eines LSTM sind solche Vorhersagen möglich.

**LSTM** steht für *Long Short-Term Memory*

Das Problem: Normale KNNs haben kein Gedächtnis - sie vergessen daher sofort, was sie gerade gesehen haben.

Ein LSTM kann sich wichtige Informationen merken und unwichtige vergessen.

LSTMs sind eine faszinierende Technik und der Name ist Programm:

Long Short Term Memory

Also ein Lang- und ein Kurzzeitgedächtnis für Begriffe.

Weniger wichtige Fakten, z.B. der Satzbau des zuletzt analyisierten Satzes, werden gleich wieder vergessen.

Wichtige Begriffe, wie ein Hauptwort, werden länger gemerkt, so dass sie zu einem späteren Zeitpunkt während der Analyse noch zur Verfügung stehen.

Doch wie kann sich ein KNN überhaupt etwas merken?

Dafür sind die Recurrent Neural Networks zuständig. Sie können sich einen Zustand merken.

Dieser wird als Teil des Modells gespeichert und nicht in externen Variablen.

Der Begriff "Reccurrent" steht für "wieder - laufend" also zurücklaufend und damit im übertragenen Sinne für eine Rückkopplungsschleife. Über sie wird

die Ausgabe (bzw. der Zustand) eines Zeitschritts beim nächsten Schritt wieder als Eingang verwendet.

Normale (Feedforward-)Netze sehen jeden Input isoliert, ohne Kontext.

Ein RNN dagegen merkt sich frühere Zustände.

```
x₁ → h₁
x₂ + h₁ → h₂
x₃ + h₂ → h₃
```

h1 wird rekurrent weitergegeben an h2.

Dadurch erhält das Netzwerk ein Gedächtnis.

Zurück zu den LSTMs und ihren Merkmalen ein Kurz- und ein Langzeitgedächtnis zu besitzen.

**Beispiel:**

Text: "Tom arbeitet als Programmierer. Er schreibt Code für eine App. 
       Dann testet er seine Arbeit am Computer."

Ein *LSTM* verarbeitet diesen Text wie folgt:

LSTM beim Verarbeiten:

"Tom arbeitet als Programmierer" → MERKEN: Hauptperson = Tom, Beruf = Programmierer
"Er schreibt Code" → ERINNERN: "Er" = Tom, MERKEN: Aktivität = Code schreiben
"für eine App" → MERKEN: Zweck der Arbeit = App
"Dann testet er" → ERINNERN: "er" = Tom, VERGESSEN: "schreiben" (neue Phase), MERKEN: neue Aktivität = testen
"seine Arbeit" → ERINNERN: "seine" = Toms Arbeit (der Code von vorhin)
"am Computer" → MERKEN: Arbeitsplatz/Werkzeug

Ein LSTM arbeitet mit 3 Türen:

1. Forget Gate (Vergiss-Tür)

Aufgabe: "Was soll ich vergessen?"

Entscheidet, welche alte Information gelöscht wird 
Öffnet sich, wenn alte Info nicht mehr wichtig ist

Beispiel:

"Tom schreibt Code. Dann testet er..."

Bei "Dann testet" → Forget Gate öffnet sich → "schreibt Code" wird vergessen

2. Input Gate (Eingabe-Tür)

Aufgabe: "Was soll ich neu speichern?"

Entscheidet, welche neue Information gespeichert wird

Öffnet sich, wenn neue Info wichtig ist

Beispiel:

"Dann testet er seine Arbeit"

Bei "testet" → Input Gate öffnet sich → "testet" wird als neue wichtige Info gespeichert

3. Output Gate (Ausgabe-Tür)
Aufgabe: "Was soll ich weitergeben?"

Entscheidet, welche gespeicherte Information ausgegeben wird
Öffnet sich, wenn gespeicherte Info jetzt relevant ist

Beispiel:

"Er testet seine Arbeit"

Bei "er" → Output Gate öffnet sich → Tom-Information wird ausgegeben für Pronomen-Bezug

Wie die Türen zusammenarbeiten:

Schritt 1: Forget Gate  → Alte unwichtige Info löschen
Schritt 2: Input Gate   → Neue wichtige Info speichern  
Schritt 3: Output Gate  → Relevante Info weitergeben

Diese 3 Türen machen das LSTM so mächtig - es kann selektiv vergessen, lernen und erinnern! 

Bleiben wir beim ersten Satz:

"Tom arbeitet als Programmierer"

Wie kann das LSTM erkennen, dass "Tom" eine Person und "Programmierer" eine Berufsbezeichnung ist?

Die Antwort: Gar nicht.

Das LSTM hat (natürlich) keine Ahnung, was diese Wörter bedeuten!

Das LSTM erkennt nicht direkt, dass Tom eine Person und Programmierer ein Beruf ist. Es lernt Muster aus vielen Beispielen.

Was das LSTM wirklich sieht ist eine Liste mit Zahlen:

Input: [45, 123, 67, 892]  // Zahlen für "Tom", "arbeitet", "als", "Programmierer"

Das LSTM lernt vielmehr Muster:

"Tom arbeitet als Programmierer"
"Lisa arbeitet als Ärztin" 
"Max arbeitet als Lehrer"
"Anna arbeitet als Designerin"

Das LSTM erkennt Muster:

Muster 1: [Wort] + "arbeitet als" + [Wort]

Erstes Wort kommt später oft als "er/sie" vor
Letztes Wort kommt in ähnlichen Kontexten vor

Muster 2: Grammatische Position

Position 1: Wird später durch Pronomen ersetzt → "wichtig zum Merken"
Position 4: Steht nach "als" → "beschreibt das erste Wort"

Was passiert intern:
"Tom" → Input Gate öffnet sich → "Position-1-Wort speichern"
"arbeitet" → "Verb erkannt, Subjekt wird wichtig"  
"als" → "Nächstes Wort beschreibt Subjekt"
"Programmierer" → Input Gate öffnet sich → "Beschreibung von Position-1-Wort"

Das LSTM lernt statistische Zusammenhänge, nicht Bedeutung! Es "merkt" sich Tom, weil es gelernt hat: "Das erste Wort in diesem Muster wird später wieder gebraucht.

Autoregressiv bedeutet, dass ein Modell seine eigenen vorherigen Ausgaben als Eingabe für die nächste Vorhersage verwendet.

In einem autoregressiven Language Model wird jedes neue Wort basierend auf den bereits generierten Wörtern vorhergesagt. Der Prozess läuft so ab:

Start: "The weather is"
Vorhersage 1: Modell sagt "very" vorher → "The weather is very"
Vorhersage 2: Modell nutzt "The weather is very" und sagt "cold" vorher → "The weather is very cold"
Vorhersage 3: Modell nutzt "The weather is very cold" und sagt "today" vorher → "The weather is very cold today"

Das Modell berechnet die Wahrscheinlichkeit des nächsten Wortes basierend auf der Sequenz:

```
P(Wort_n | Wort_1, Wort_2, ..., Wort_n-1)
```

Vorteile:
- Kohärente, zusammenhängende Textgenerierung
- Jedes Wort baut auf dem vorherigen Kontext auf

Nachteile:
- Sequenzielle Generierung (nicht parallelisierbar)
- Fehler können sich durch die Sequenz "fortpflanzen"

### Perplexity

Perplexity ist ein Maß dafür, wie "verwirrt" oder "unsicher" ein Language Model bei der Vorhersage des nächsten Wortes ist. Je niedriger die Perplexity, desto besser das Modell.

Perplexity ist ein standardisiertes Bewertungsmaß für Language Models.

Sehr gute Modelle haben eine Perplexity von 20 bis 50, schlechte Modelle eine Perplexity größer 500.

Stelle Dir vor, das Modell muss bei jedem Wort raten:

- Niedrige Perplexity: Das Modell ist sich ziemlich sicher, welches Wort als nächstes kommt
- Hohe Perplexity: Das Modell ist verwirrt und muss zwischen vielen möglichen Wörtern "raten"

Mathematische Definition

```
Perplexity = 2^(-1/N * Σ log₂(P(wᵢ)))
```

Beispiel:

Satz: "The weather is very..."

Gutes Modell:

- P("cold") = 0.7
- P("hot") = 0.2
- P("nice") = 0.1
- → Niedrige Perplexity (~2-3)

Schlechtes Modell:

- Alle 10.000 Wörter im Vokabular haben gleiche Wahrscheinlichkeit (0.0001)
- → Hohe Perplexity (~10.000)

|Perplexity|Bedeutung|
|----------|---------|
|100       |Das Modell ist so unsicher, als müsste es bei jedem Wort zwischen 100 gleichwahrscheinlichen Optionen wählen|
|10        |Das Modell kann die Auswahl auf etwa 10 wahrscheinliche Wörter eingrenzen|
|2         |Das Modell schwankt meist nur zwischen 2 wahrscheinlichen Optionen|


