' Vorhersage der Prüfungsergebnisse anhand der Anzahl der Studien- und Schlafstunden
' Die Eingabe besteht aus zwei Merkmalen: Studienstunden und Schlafstunden
' Die Ausgabe ist eine binäre Klassifikation: 1 (Bestanden) oder 0 (Durchgefallen)

Module PerceptronExample
    ' Define perceptron weights and bias
    Dim weights() As Double = {0.0, 0.0} ' Two inputs: Study hours and Sleep hours
    Dim bias As Double = 0.0
    Dim learningRate As Double = 0.1

    Sub Main()
        ' Training data: {study_hours, sleep_hours}
        Dim inputs(,) As Double = {
            {2, 1}, {3, 1.5}, {5, 2}, {6, 2.5}
        }
        Dim outputs() As Integer = {0, 0, 1, 1}

        ' Train the perceptron
        Console.WriteLine("Training the perceptron...")
        For epoch As Integer = 1 To 10 ' Number of training iterations
            Dim totalError As Integer = 0

            For i As Integer = 0 To 3
                ' Get inputs and expected output
                Dim x1 As Double = inputs(i, 0)
                Dim x2 As Double = inputs(i, 1)
                Dim expected As Integer = outputs(i)

                ' Compute the perceptron output
                Dim prediction As Integer = Predict(x1, x2)

                ' Calculate the error
                Dim error As Integer = expected - prediction
                totalError += Math.Abs(error)

                ' Update weights and bias using the perceptron learning rule
                weights(0) += learningRate * error * x1
                weights(1) += learningRate * error * x2
                bias += learningRate * error
            Next

            ' Display progress
            Console.WriteLine($"Epoch {epoch}: Total Error = {totalError}")

            ' Stop early if the perceptron has learned the pattern
            If totalError = 0 Then Exit For
        Next

        ' Test the perceptron
        Console.WriteLine("Testing the perceptron...")
        Dim testInputs(,) As Double = {
            {2.5, 1}, {4, 1.5}, {6, 3}, {3, 0.5}
        }
        For i As Integer = 0 To testInputs.GetLength(0) - 1
            Dim x1 As Double = testInputs(i, 0)
            Dim x2 As Double = testInputs(i, 1)
            Dim result As Integer = Predict(x1, x2)
            Console.WriteLine($"Input: Study Hours={x1}, Sleep Hours={x2} => Output: {(If(result = 1, "Pass", "Fail"))}")
        Next
    End Sub

    ' Function to compute perceptron output
    Function Predict(x1 As Double, x2 As Double) As Integer
        Dim sum As Double = weights(0) * x1 + weights(1) * x2 + bias
        Return If(sum > 0, 1, 0) ' Step activation function
    End Function

End Module
