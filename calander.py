import PySimpleGUI as sg
import time
import keyboard

def CountLines(): #count the number of lines in the excuse list
    with open(r"excusesList.txt", "r") as file:
        for LineCount, line in enumerate(file):
            pass
    return LineCount
LineCount = CountLines()
RollOverNumber = LineCount + 1
def calander(): #the stuff that go BRRRRRRRR
        file = open("calanderMemory.txt", 'r') #open the memory to find the line that was left off at previously
        LineNumA = file.readline() #read the thingymabob as a string
        LineNum = int(LineNumA) #make string an integer through voodoo
        LineNumB = LineNum + 1 #add 1 so that there are no repeats and it properly counts
        LineNumNew = str(LineNumB) #turn it back into a string by sacrificing a goat
        file.close() #close the memory file
        if (int(LineNumNew) >= RollOverNumber): #make sure the program doesnt count too high
            LineNumNew = "0" #if it has counted too high smack it down to 0
            print("rolled over") #testing shit to make sure it still works
        file= open("calanderMemory.txt", 'w') #open the memory so that it can be brainwashed
        file.writelines(LineNumNew) #overwrite with commpletly new data
        file.close() #close the file
        file = open("excusesList.txt") #open the excuses repository
        Data = file.readlines() #yoink them into a variable
        FullData = file.readlines() #i dont remember what this does
        file.close() #close the file before the user can break it


        return Data[LineNum]
        return LineNum
        return FullData
        return LineCount
Data = calander() #tell program that this should have a value

layout = [  [sg.Text(text = calander(), key = "textBox")],    #make fancy bits look fancy
            #[sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Next'), sg.Button('Exit'), sg.Button('Add Excuse')] ]
window = sg.Window('Excuse Calender', layout, return_keyboard_events = True) #rename fancy bits and poof them into existance

while True: #checks if while is spelled properly
    event, values = window.read() #finds out who is touching shit
    if event == sg.WIN_CLOSED or event == 'Exit': #cuts power to program
        break #declares coffee break
    if event == 'Next': #makes the next button go brrrrrr
        #print("next") #tells izzy if he is crazy or if its working
        window["textBox"].update(calander()) #trys to update text box
        window.refresh() #trys to update text box
    if event == 'Add Excuse': #lets user add more communist era propaganda to the dumpster fire
        file = open("excusesList.txt") #opens the excuses
        FullData = file.readlines() #illegally downloads all current excuses
        file.close() #im not explaining this see line 28
        file = open("excusesList.txt", "a") #grants admin permissions to the machine
        NewExcuse = input('Please Type Your New Excuse In The EXACT FORMAT You Wish For It To Be Added ') #screams at user
        file.write(NewExcuse+'\n') #rewrites sanitized excuses to file
        file.close() # see line 54
    if keyboard.read_key() == "q": #stops izzy from breaking his cmd terminal
        break
    #if input() == "exit":
    #    print("a")
    #if key == Key.delete:
    #    print("You pressed 'Delete'.")
            #window.close()
    #    break
    #if keyboard.read_key() == "q":
    #    break
    #time.sleep(1)
    #window["textBox"].update(Data)
    window.refresh()

window.close()
