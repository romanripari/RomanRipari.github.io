VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} ProgressBar 
   Caption         =   "Plan Táctico TV | Processes & Innovation"
   ClientHeight    =   3015
   ClientLeft      =   90
   ClientTop       =   360
   ClientWidth     =   5550
   OleObjectBlob   =   "ProgressBar.frx":0000
   ShowModal       =   0   'False
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "ProgressBar"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub lbl_Logo_Click()

End Sub

Private Sub ToggleButton1_Click()
    BarraDeProgreso.Cancelar
End Sub

Private Sub UserForm_Initialize()
'    Me.Progreso.BackColor = RGB(51, 102, 153)
'    Me.ProgresoLabel.BackColor = RGB(255, 255, 255)
'    Me.Label4.BackColor = RGB(230, 230, 230)
    Me.BackColor = RGB(255, 255, 255)
    Me.LabelTitulo.BackColor = RGB(255, 255, 255)
    Me.StartUpPosition = 2
End Sub

Private Sub UserForm_QueryClose(Cancel As Integer, CloseMode As Integer)
    If CloseMode = 0 And Progresando = True Then
        Cancel = 1
    End If
End Sub
