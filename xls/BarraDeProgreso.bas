Attribute VB_Name = "BarraDeProgreso"
Option Explicit

Public dTotal As Double
Public dAvance As Double
Public strLabel As String
Public Progresando As Boolean

' ----------------------------------------------------------------
'Este módulo junto con el formulario "Progress Bar" debe ser importado en el excel en que utilizará
'Ejemplo de como utilizar esta función:
Function Ejemplo()
    Dim Maximo As Double, f As Double
    Maximo = 12345
    BarraDeProgreso.IniciaBarra Maximo, "Acá escribimos un título..."
    For f = 1 To Maximo
        BarraDeProgreso.AvanzaBarra
        If f > 1000 Then BarraDeProgreso.Subtitulo "Subtítulo: Van más de 1000.."
        If f > 3000 Then BarraDeProgreso.Subtitulo "Otro subtítulo: Van más de 3000.."
        If f > 5000 Then BarraDeProgreso.Subtitulo "Subtítulo: Van más de 5000.."
        If f > 7000 Then BarraDeProgreso.Subtitulo "Otro subtítulo: Van más de 7000.."
    Next
    BarraDeProgreso.Cierra
End Function
' ----------------------------------------------------------------
'Description: Función para crear objeto de form con un texto y un número máximo, como 100%
'Created: Román Ripari
'Edited: -
'Last modified: '8/11/19
' ----------------------------------------------------------------
Function IniciaBarra(iTotal As Double, strLabel As String)
If iTotal <> 0 Then
    dAvance = 0
    dTotal = iTotal
    ProgressBar.Show
    ProgressBar.LabelTitulo = strLabel
    ProgressBar.Progreso.Width = dAvance / dTotal
    ProgressBar.Subtitulo = ""
    Progresando = True
End If
End Function
' ----------------------------------------------------------------
'Description: Función para avanzar un punto en el porcentaje del form
'Created: Román Ripari
'Edited: -
'Last modified: '8/11/19
' ----------------------------------------------------------------
Function AvanzaBarra()
dAvance = dAvance + 1
ProgressBar.Progreso.Width = dAvance / dTotal * 260
'***************************** Con cantidad y porcentaje*****************
'ProgressBar.ProgresoLabel.Caption = dAvance & " de " & dTotal & "   -   " & Format(dAvance / dTotal, "0.0%")
'***************************** Solo Con cantidad*****************
'ProgressBar.ProgresoLabel.Caption = dAvance & " de " & dTotal
'***************************** solo con porcentaje*****************
ProgressBar.ProgresoLabel.Caption = Format(dAvance / dTotal, "0.0%")
DoEvents
End Function
' ----------------------------------------------------------------
'Description: Función para cerrar el formulario
'Created: Román Ripari
'Edited: -
'Last modified: '8/11/19
' ----------------------------------------------------------------
Function Cierra()
    BarraDeProgreso.Completa100
    Application.Wait Now + #12:00:01 AM#
    Progresando = False
    dAvance = 0
    Unload ProgressBar
End Function

Function Subtitulo(sSubt As String)
    
    ProgressBar.Subtitulo = sSubt
    DoEvents

End Function

Function Completa100()
Dim Resto As Double
For Resto = dAvance + 1 To dTotal
    BarraDeProgreso.AvanzaBarra
Next
End Function

Function Cancelar()
Dim a As Byte
    a = MsgBox("¿Desea cancelar el proceso?", vbExclamation + vbYesNo, "Plan Táctico TV | Processes & Innovation")
    If a = 6 Then
        End
    End If
End Function



