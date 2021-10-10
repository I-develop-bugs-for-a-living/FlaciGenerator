from tkinter import *
import json
import random
import string
import itertools as it

def generating():
    nodeList = {}
    nodeList['X'+"0"*int(numPlatten.get())] = ['X', (0, 0), 1,'q0', [createTransition(1,1,0,0,["+", "-"])], True, "X" + "0"*int(numPlatten.get())]
    alphabet, platten = createAlphabetPlatten()
    # startNode = createState(id=1, name="q0", transitions=[], start=True, output=outputstring)
    stufenList = [str(x) for x in range(int(numStufen.get()))]
    positionList = {key: value for value, key in enumerate(platten)}
    states = []
    
    counter = 1
    for i in range(int(numPlatten.get())):
        letter = string.ascii_uppercase[i]
        for i in it.product(stufenList, repeat=int(numPlatten.get())):
            # nodeList[output/idcode] = [startingletter, numbercode, id, name, transitions, startnode, output/idcode]
            nodeList[f'{letter}'+''.join(i)] = [letter, i, counter+1,f'q{counter}', [], False, f'{letter}'+''.join(i)]
            counter += 1
    
    print(nodeList)

    for i in nodeList:
        activeLetter = i[0]
        numberCode = i[1:]
        for j in platten:
            if activeLetter != j:
                nodeList[i][4].append(createTransition(nodeList[i][2], nodeList[j+numberCode][2], 0,0,[j]))
            if activeLetter == j:
                nodeList[i][4].append(createTransition(nodeList[i][2], nodeList[i][2], 0,0, [j]))
        
        if activeLetter != 'X':
            position = positionList[activeLetter]
            if int(numberCode[position])-1 >= 0:
                node = activeLetter + mutateString(numberCode, position, str(int(numberCode[position])-1))
                nodeList[i][4].append(createTransition(nodeList[i][2], nodeList[node][2], 0,0,"-"))
            else:
                nodeList[i][4].append(createTransition(nodeList[i][2], nodeList[i][2], 0,0,"-"))
            if int(numberCode[position])+1<int(numStufen.get()):
                node = activeLetter + mutateString(numberCode, position, str(int(numberCode[position])+1))
                nodeList[i][4].append(createTransition(nodeList[i][2], nodeList[node][2], 0,0, "+"))
            else:
                nodeList[i][4].append(createTransition(nodeList[i][2], nodeList[i][2], 0,0,"+"))

    for i in nodeList:
        states.append(createState(nodeList[i][2], nodeList[i][3], nodeList[i][4], nodeList[i][5], nodeList[i][6]))
    
    layout = createLayout(alphabet, states)

    x = json.dumps(layout)

    with open("output.json", "w") as f:
        f.write(x)

def mutateString(string, position, replacement):
    temp = list(string)
    temp[position] = replacement
    temp = "".join(temp)
    return temp
    
def createAlphabetPlatten():
    alph = []
    platten = []
    for i in range(int(numPlatten.get())):
        alph.append(string.ascii_uppercase[i])
        platten.append(string.ascii_uppercase[i])
    alph.append("+")
    alph.append("-")
    return alph, platten

def createLayout(alphabet, states):
    dictLayout = {"name": "NEF Cookingstation",
            "description": "200",
            "type": "MOORE",
            "automaton": {
                "acceptCache": [],
                "simulationInput": [],
                "Alphabet": alphabet,
            "StackAlphabet": [
                "|"
            ],
            "States": states,
            "lastInputs": []
        }
    }
    return dictLayout

def createState(id, name, transitions, start, output):
    dictState = {
        "ID": id,
        "Name": name,
        "x": random.randint(0, 1000),
        "y": random.randint(0, 1000),
        "Final": False,
        "Radius": 30,
        "Transitions": transitions,
        "Start": start,
        "Output": output,
    }
    return dictState

def createTransition(source, target, x, y, labels):
    dictTransition = {
        "Source": source,
        "Target": target,
        "x": x,
        "y": y,
        "Labels": labels
    }
    return dictTransition


screen = Tk()
screen.title("Moore-Automaten-Generator")

# vatiables
numPlatten = StringVar()
numStufen = StringVar()

header = Label(text="HerdplattenGenerator", font=("Arial", 32))
plattenLable = Label(text="Enter # Platten:")
stuffenLable = Label(text="Enter # Stuffen:")

entryNumPlatten = Entry(textvariable=numPlatten)
entryNumStuffen = Entry(textvariable=numStufen)

startButton = Button(text="Start generating...", command=generating)

header.grid(row=0, column=0, columnspan=2)
plattenLable.grid(row=1, column=0)
stuffenLable.grid(row=1, column=1)
entryNumPlatten.grid(row=2, column=0)
entryNumStuffen.grid(row=2, column=1)
startButton.grid(row=3, column=0, columnspan=2)

screen.mainloop()