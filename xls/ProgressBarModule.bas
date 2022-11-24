Attribute VB_Name = "ProgressBarModule"
Option Explicit

' ----------------------------------------------------------------
'Created: Roman Ripari
'https://romanripari.ar
'Edited by: -
'Last modified: '23/11/2022
' ----------------------------------------------------------------
' You have to import this module and the form called "Progress Bar" into your Excel file, through VBA Editor

Public dTotal As Double
Public dProgress As Double
Public strLabel As String
Public Progresando As Boolean

' ----------------------------------------------------------------
' Example:
' ----------------------------------------------------------------
Function Example()
    Dim dMax As Double, f As Double
    dMax = 12345
    
    ProgressBarModule.StartBar dMax, "Here we write a title..."
    For f = 1 To dMax
        ProgressBarModule.IncreaseBar
        If f < 1000 Then
            ProgressBarModule.Subtitle "Subtitle: less than 1000.."
        ElseIf f < 3000 Then
            ProgressBarModule.Subtitle "Subtitle: less than 3000.."
        ElseIf f < 5000 Then
            ProgressBarModule.Subtitle "Subtitle: less than 5000.."
        Else
            ProgressBarModule.Subtitle "Subtitle: more than 5000.."
        End If
    Next
    ProgressBarModule.CloseBar
End Function

' ----------------------------------------------------------------
'Description: Function to create a form object with a text as title and a maximun number as 100%
' ----------------------------------------------------------------
Function StartBar(iTotal As Double, strLabel As String)
If iTotal <> 0 Then
    dProgress = 0
    dTotal = iTotal
    ProgressBar.Show
    ProgressBar.LabelTitle = strLabel
    ProgressBar.Progress.Width = dProgress / dTotal
    ProgressBar.Subtitle = ""
    Progresando = True
End If
End Function

' ----------------------------------------------------------------
'Description: Function to increase +1 and show the new result
' ----------------------------------------------------------------
Function IncreaseBar()
dProgress = dProgress + 1
ProgressBar.Progress.Width = dProgress / dTotal * 260

'*** Amount and Percentage ***
'ProgressBar.ProgressLabel.Caption = dProgress & " de " & dTotal & "   -   " & Format(dProgress / dTotal, "0.0%")

'*** Only Amount ***
'ProgressBar.ProgressLabel.Caption = dProgress & " de " & dTotal

'*** Only Percentage ***
ProgressBar.ProgressLabel.Caption = Format(dProgress / dTotal, "0.0%")

DoEvents
End Function

' ----------------------------------------------------------------
'Description: Function to complete 100% and close the Form
' ----------------------------------------------------------------
Function CloseBar()
    ProgressBarModule.Complete100
    Application.Wait Now + #12:00:01 AM#
    Progresando = False
    dProgress = 0
    Unload ProgressBar
End Function

' ----------------------------------------------------------------
'Description: Function to change the subtitle
' ----------------------------------------------------------------
Function Subtitle(sSubt As String)
    ProgressBar.Subtitle = sSubt
    DoEvents
End Function

' ----------------------------------------------------------------
'Description: Function to rapidly complete 100% before close
' ----------------------------------------------------------------
Function Complete100()
Dim Remains As Double
For Remains = dProgress + 1 To dTotal
    ProgressBarModule.IncreaseBar
Next
End Function

' ----------------------------------------------------------------
'Description: Function to kill any running process
' ----------------------------------------------------------------
Function CancelarProgress()
Dim a As Byte
    a = MsgBox("Do you want to cancel the process?", vbExclamation + vbYesNo, "")
    If a = 6 Then
        End
    End If
End Function
