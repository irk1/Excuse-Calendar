import PySimpleGUI as sg
import time
import keyboard
#on startup read memory file to find which line was left off at +1 to the number and set internal variable LineNum to it and read the excuse on the line equal to LineNum
#open data file
def CountLines():
    with open(r"TestText.txt", "r") as file:
        for LineCount, line in enumerate(file):
            pass
    return LineCount
LineCount = CountLines()
RollOverNumber = LineCount + 1
def calander():
        file = open("calanderMemory.txt", 'r')
#read memory as string
        LineNumA = file.readline()
#convert string to integer

        LineNum = int(LineNumA)
        LineNumB = LineNum + 1
        LineNumNew = str(LineNumB)
        file.close()
        if (int(LineNumNew) >= RollOverNumber):
            LineNumNew = "0"
            print("rolled over")


        file= open("calanderMemory.txt", 'w')
        file.writelines(LineNumNew)
        file.close()
        file = open("excusesList.txt")
        Data = file.readlines()
        FullData = file.readlines()
        file.close()

        print(LineCount)
        #print("LineNumA= " + LineNumA)
        #print("LineNum= " + str(LineNum))
        #print("LineNumB= " + str(LineNumB))
        #print("LineNumNew= " + LineNumNew)
        #print(Data[LineNum])
        return Data[LineNum]
        return LineNum
        return FullData
        return LineCount
#print(Data[0])
Data = calander()

#def GUI():
layout = [  [sg.Text(text = calander(), key = "textBox")],
            #[sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Next'), sg.Button('Exit'), sg.Button('Add Excuse(WIP)')] ]
#GUI()

window = sg.Window('Excuse Calender', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event == 'Next': #makes the next button go brrrrrr
        #print("next")
        window["textBox"].update(calander())
        window.refresh()
    if event == 'Add Excuse(WIP)':
        file = open("excusesList.txt")
        FullData = file.readlines()
        file.close()
        file = open("TestText.txt", "a")
        #print('Please Type Your New Excuse In The EXACT FORMAT You Wish For It To Be Added')
        NewExcuse = input('Please Type Your New Excuse In The EXACT FORMAT You Wish For It To Be Added ')
        #file.seek(0,2)
        file.write(NewExcuse+'\n')
        file.close()

    #if input() == "exit":
    #    print("a")
    #if keyboard.read_key() == "q":
    #    break
    #time.sleep(1)
    #window["textBox"].update(Data)
    window.refresh()

window.close()
