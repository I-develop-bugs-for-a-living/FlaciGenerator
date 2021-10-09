from tkinter import *
import json
import random
import string
import itertools as it

def generating():
    nodeList = []
    nodeList.append(['x', (0, 0), 'q0', [], True, "x" + "0"*int(numPlatten.get())])
    alphabet = createAlphabet()
    # startNode = createState(id=1, name="q0", transitions=[], start=True, output=outputstring)
    stufenList = [str(x) for x in range(int(numStufen.get()))]
    states = []
    
    counter = 1
    for i in range(int(numPlatten.get())):
        letter = string.ascii_lowercase[i]
        for i in it.product(stufenList, repeat=int(numPlatten.get())):
            nodeList.append([letter, i, f'q{counter}', [], False, f'{letter}'+''.join(i)])
            counter += 1
    
    print(nodeList)

    for i in nodeList:
        pass
            
    layout = createLayout(alphabet, states)

    x = json.dumps(layout)

    with open("output.json", "w") as f:
        f.write(x)
    
def createAlphabet():
    alph = []
    for i in range(int(numPlatten.get())):
        alph.append(string.ascii_uppercase[i])
    for i in range(int(numStufen.get())):
        alph.append(str(i))
    return alph

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