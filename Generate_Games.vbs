Set action_play = createobject("WScript.shell")

action_play.AppActivate "Quackle versus New Player 1 - Quackle"

path_play = "C:\Users\curley1\Documents\IndependentStudy\QStuff\"

For n = 1 To 2566
    
    action_play.sendkeys "^n", 1
    action_play.SendKeys "~", 1
    
    WScript.sleep 5000
    
    action_play.sendkeys "^s", 1
    WScript.sleep 1000
    action_play.SendKeys path_play & "Game_Number_" & n & ".gcg", 1
    WScript.sleep 1000
    action_play.SendKeys "~", 1
    WScript.sleep 1000
    
    action_play.SendKeys "%p", 1
    action_play.SendKeys "{DOWN}", 1
    action_play.SendKeys "{DOWN}", 1
    action_play.SendKeys "{DOWN}", 1
    action_play.SendKeys "~", 1
    
    WScript.sleep 1000
    action_play.SendKeys path_play & "Report_Number_" & n & ".txt", 1
    WScript.sleep 1000
    action_play.SendKeys "~", 1

    WScript.sleep 5000
Next 