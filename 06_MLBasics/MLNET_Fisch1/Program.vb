' Fisch-Klassifizierung mit einem einfachen binären Klassifikator
' Erstellt: 13/12/24

Imports Microsoft.ML
Imports Microsoft.ML.Data

Imports System.IO

Class FishData
    <LoadColumn(0)>
    Public Property Length As Single
    <LoadColumn(1)>
    Public Property Density As Single
    <LoadColumn(2)>
    Public Property FishType As Boolean
End Class

Class FishPrediction
    <ColumnName("PredictedLabel")>
    Public Property PredictedLabel As Boolean
    Public Property Probability As Single
    Public Property Score As Single
End Class

Module Program

    Sub Main()
        ' MLContext ist die zentrale Klasse für die ML.NET-Bibliothek
        Dim mlContext As New MLContext

        ' Trainingsdaten laden
        Dim csvPath = Path.Join(Environment.CurrentDirectory, "..", "data", "fish-data.csv")
        Dim fishData As IDataView = mlContext.Data.LoadFromTextFile(Of FishData)(
            csvPath, separatorChar:=","c, hasHeader:=True)

        ' Trainingsdaten und Testdaten abzweigen
        Dim dataSplit = mlContext.Data.TrainTestSplit(fishData, testFraction:=0.2)
        Dim trainData As IDataView = dataSplit.TrainSet
        Dim testData As IDataView = dataSplit.TestSet

        ' Pipeline definieren
        Dim Pipeline = mlContext.Transforms.CopyColumns("Label", "FishType") _
         .Append(mlContext.Transforms.Concatenate("Features", "Length", "Density")) _
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
        Dim modelPath = Path.Join(Environment.CurrentDirectory, "..", "Data", "FishClassifier.zip")
        mlContext.Model.Save(model, trainData.Schema, modelPath)

        Console.WriteLine("Modell gespeichert.")

        ' Model wieder laden
        Dim loadedModel As ITransformer
        Using fs = new FileStream(modelPath, FileMode.Open, FileAccess.Read)
            loadedModel = mlContext.Model.Load(fs, inputSchema := Nothing)
            Console.WriteLine("Model wurde geladen.")
        End Using
 
        ' Vorhersage treffen
        Dim predictionEngine = mlContext.Model.CreatePredictionEngine(Of FishData, FishPrediction)(loadedModel)

        Dim fish1 = New FishData With {.Length = 25.4F, .Density = 0.98F}
        Dim fish2 = New FishData With {.Length = 26.3F, .Density = 0.98F}

        Dim prediction1 = predictionEngine.Predict(fish1)
        Dim prediction2 = predictionEngine.Predict(fish2)

        Console.WriteLine($"Fisch 1: {prediction1.PredictedLabel}")
        Console.WriteLine($"Fisch 2: {prediction2.PredictedLabel}")

    End Sub

End Module