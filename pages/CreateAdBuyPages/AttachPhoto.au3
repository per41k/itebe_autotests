WinWaitActive("�������")
Sleep(10000)
ControlClick("�������", "", "Edit1")
Sleep(500)
WinWaitActive("�������", "", 1)
Send("C:\Users\User\Documents\Photo{ENTER}")
Sleep(500)
Send("O_TGxQBcI5M{ENTER}")
WinWaitClose("�������", "", 1)