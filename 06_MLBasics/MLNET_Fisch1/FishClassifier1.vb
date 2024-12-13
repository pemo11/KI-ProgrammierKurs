' Fisch-Kategorisierung mit einem einfachen binären Klassifikator
' Erstellt: 13/12/24
Imports Microsoft.ML
Imports Microsoft.ML.Data

Module Program

    Sub Main()
        ' MLContext ist die zentrale Klasse für die ML.NET-Bibliothek
        Dim mlContext As New MLContext

        ' Trainingsdaten laden
        Dim csvPath = Path.Join(Environment.CurrentDirectory, "Data", "fish-data.csv")
        Dim fishData As IDataView = mlContext.Data.LoadFromTextFile(Of FishData)(
            csvPath, separatorChar:=","c, hasHeader:=True)

        ' Trainingsdaten und Testdaten abzweigen
        Dim dataSplit = mlContext.Data.TrainTestSplit(fishData, testFraction:=0.2)
        Dim trainData As IDataView = dataSplit.TrainSet
        Dim testData As IDataView = dataSplit.TestSet

        ' Pipeline definieren
        Dim Pipeline = mlContext.Transforms.Concatenate("Features", "Length", "Density") _
         .Append(mlContext.BinaryClassification.Trainers.SdcaLogisticRegression())

        ' Modell trainieren
        Dim model = Pipeline.Fit(trainData)

        ' Testdaten auswerten
        Dim predictions = model.Transform(testData)

        ' Metriken berechnen
        Dim metrics = mlContext.BinaryClassification.Evaluate(predictions)

        ' Ausgabe der Metriken
        Console.WriteLine($"Accuracy: {metrics.Accuracy}")
        Console.WriteLine($"AUC: {metrics.AreaUnderRocCurve}")
        Console.WriteLine($"F1-Score: {metrics.F1Score}")

        ' Modell speichern
        Dim modelPath = Path.Join(Environment.CurrentDirectory, "Data", "FishClassifier.zip")
        mlContext.Model.Save(model, trainData.Schema, modelPath)

        Console.WriteLine("Modell gespeichert.")

        ' Vorhersage treffen
        Dim predictor = mlContext.Model.Load(modelPath, out var modelSchema)
        Dim predictionEngine = mlContext.Model.CreatePredictionEngine(Of FishData, FishPrediction)(predictor)

        Dim fish1 = New FishData With {.Length = 25.4F, .Density = 0.98F}
        Dim fish2 = New FishData With {.Length = 26.3F, .Density = 0.98F}

        Dim prediction1 = predictionEngine.Predict(fish1)
        Dim prediction2 = predictionEngine.Predict(fish2)

        Console.WriteLine($"Fisch 1: {prediction1.Prediction}")
        Console.WriteLine($"Fisch 2: {prediction2.Prediction}")