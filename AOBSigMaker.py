import tkinter as tk  # python3
from tkinter import GROOVE, ttk
from tkinter.scrolledtext import ScrolledText
from ttkthemes import ThemedTk


def Refresher():
    Footer.config(
        text="- click above output boxes for copy to clipboard -", fg='gray66')
    app.after(1500, Refresher)


def add_highlight(line, text):
    inputAOB.tag_add("miss", line, line + (len(text) * 0.1))
    inputAOB.tag_config("miss", background="maroon", foreground="white")


def read():
    readLines.clear()
    incorrect = {}
    i = 1.0
    lines = inputAOB.get(1.0, "end").splitlines()
    tempLine = lines[0]
    for line in lines:
        if line != '' and len(line) == len(tempLine):
            readLines.append(line)
            i = i + 1.0
        else:
            incorrect[i] = line
            i = i + 1.0
    inputAOB.tag_remove("miss", 1.0, "end")
    for i in incorrect.keys():
        add_highlight(i, incorrect[i])


def calcResultDigit():
    RESULT = ""
    tempLine = ""
    if readLines:
        tempLine = readLines[0]
        for line in readLines:
            RESULT = ""
            for i in range(0, len(line), 1):
                if tempLine[i].lower() != line[i].lower():
                    RESULT = RESULT + "?"
                else:
                    RESULT = RESULT + tempLine[i].upper()
            tempLine = RESULT
    o["ResultDigit"] = tempLine


def calcResultByte():
    RESULT = ""
    tempLine = ""
    splitedLines = []
    if readLines:
        for line in readLines:
            splitedLines.append(line.split(" "))
        tempLine = splitedLines[0]
        for i in range(0, len(tempLine), 1):
            isBreak = False
            for spLine in splitedLines:
                if spLine[i].lower() != tempLine[i].lower():
                    RESULT = RESULT + "??" + " "
                    isBreak = True
                    break
            if not isBreak:
                RESULT = RESULT + tempLine[i].upper() + " "
        # delete space from last
        tempLine = RESULT[:-1]
    o["ResultByte"] = tempLine


def calcMaskDigit():
    MASKDIGIT = ""
    tempLine = ""
    if readLines:
        tempLine = readLines[0].replace(" ", "")
        for i in range(0, len(tempLine), 1):
            isBreak = False
            for line in readLines:
                line = line.replace(" ", "")
                if tempLine[i].lower() != line[i].lower():
                    MASKDIGIT = MASKDIGIT + "?"
                    isBreak = True
                    break
            if not isBreak:
                MASKDIGIT = MASKDIGIT + "x"
    o["MaskDigit"] = MASKDIGIT


def calcMaskByte():
    MASKBYTE = ""
    tempLine = ""
    splitedLines = []
    if readLines:
        for line in readLines:
            splitedLines.append(line.split(" "))
        tempLine = splitedLines[0]
        for i in range(0, len(tempLine), 1):
            isBreak = False
            for spLine in splitedLines:
                if spLine[i].lower() != tempLine[i].lower():
                    MASKBYTE = MASKBYTE + "?"
                    isBreak = True
                    break
            if not isBreak:
                MASKBYTE = MASKBYTE + "x"
        # delete space from last
    o["MaskByte"] = MASKBYTE


def calcCstyle():
    CSTYLE = ""
    if readLines:
        BYTE = readLines[0].split(" ")
        for i in range(0, len(BYTE), 1):
            CSTYLE = CSTYLE + r'\x' + BYTE[i].upper()  # use a raw string literal
    o["Cstyle"] = CSTYLE


def calcPymemStyle():
    PYMEMSTYLE = ""
    if readLines:
        BYTE = o["ResultByte"].split(" ")
        for i in range(0, len(BYTE), 1):
            if BYTE[i] == '??':
                PYMEMSTYLE = PYMEMSTYLE + "."
            else:
                PYMEMSTYLE = PYMEMSTYLE + r'\\x' + BYTE[i].upper()  # use a raw string literal
    o["PymemStyle"] = PYMEMSTYLE


def resultbyte_clip(event):
    app.clipboard_clear()
    app.clipboard_append(o["ResultByte"])
    Footer.configure(text="Copied Result (Per Byte)", fg='goldenrod3')


def resultdigit_clip(event):
    app.clipboard_clear()
    app.clipboard_append(o["ResultDigit"])
    Footer.configure(text="Copied Result (Per Digit)", fg='goldenrod3')


def maskdigit_clip(event):
    app.clipboard_clear()
    app.clipboard_append(o["MaskDigit"])
    Footer.configure(text="Copied Mask (Per Digit)", fg='goldenrod3')


def maskbyte_clip(event):
    app.clipboard_clear()
    app.clipboard_append(o["MaskByte"])
    Footer.configure(text="Copied Mask (Per Byte)", fg='goldenrod3')


def cstyle_clip(event):
    app.clipboard_clear()
    app.clipboard_append(o["Cstyle"])
    Footer.configure(text="Copied C Style", fg='goldenrod3')


def pymemstyle_clip(event):
    app.clipboard_clear()
    app.clipboard_append(o["PymemStyle"])
    Footer.configure(text="Copied Pymem Style", fg='goldenrod3')


def printResult():
    read()
    calcResultDigit()
    calcResultByte()
    calcMaskDigit()
    calcMaskByte()
    calcCstyle()
    calcPymemStyle()

    outputResultDigit.configure(state='normal')
    outputResultByte.configure(state='normal')
    outputMaskDigit.configure(state='normal')
    outputMaskByte.configure(state='normal')
    outputCstyle.configure(state='normal')
    outputPymemStyle.configure(state='normal')

    outputResultDigit.delete(1.0, "end")
    outputResultByte.delete(1.0, "end")
    outputMaskDigit.delete(1.0, "end")
    outputMaskByte.delete(1.0, "end")
    outputCstyle.delete(1.0, "end")
    outputPymemStyle.delete(1.0, "end")

    outputResultDigit.insert(1.0, o.get("ResultDigit"))
    outputResultByte.insert(1.0, o.get("ResultByte"))
    outputMaskDigit.insert(1.0, o.get("MaskDigit"))
    outputMaskByte.insert(1.0, o.get("MaskByte"))
    outputCstyle.insert(1.0, o.get("Cstyle"))
    outputPymemStyle.insert(1.0, o.get("PymemStyle"))

    outputResultDigit.configure(state='disabled')
    outputResultByte.configure(state='disabled')
    outputMaskDigit.configure(state='disabled')
    outputMaskByte.configure(state='disabled')
    outputCstyle.configure(state='disabled')
    outputPymemStyle.configure(state='disabled')


readLines = []

o = {"ResultDigit": "",
     "ResultByte": "",
     "MaskDigit": "",
     "MaskByte": "",
     "Cstyle": "",
     "PymemStyle": ""}


# color
appBG = "gray28"
textBoxBG = "gray12"
textFG = "gray66"

# theme
app = ThemedTk(theme="equilux")

# main app config
app.title('AoB Sigmaker')
app.configure(bg=appBG)
app.geometry('500x600')
app.resizable(False, False)

# AOB box
inputAOB = ScrolledText(app, height=10, width=50,
                   bg=textBoxBG, fg='white', wrap="none", relief=GROOVE)
# Result Digit box
outputResultDigit = tk.Text(app, height=1, width=50,
                            bg=textBoxBG, fg='white', wrap="none")
# Result Byte box
outputResultByte = tk.Text(app, height=1, width=50,
                           bg=textBoxBG, fg='white', wrap="none")
# Mask Digit box
outputMaskDigit = tk.Text(app, height=1, width=50,
                          bg=textBoxBG, fg='white', wrap="none")
# Mask Byte box
outputMaskByte = tk.Text(app, height=1, width=50,
                         bg=textBoxBG, fg='white', wrap="none")
# C Style box
outputCstyle = tk.Text(app, height=1, width=50,
                       bg=textBoxBG, fg='white', wrap="none")
# Pymem Style box
outputPymemStyle = tk.Text(app, height=1, width=50,
                           bg=textBoxBG, fg='white', wrap="none")

# Signature (Array of Bytes) lebel
AOBLebel = tk.Label(width="500", text="- Signature (Array of Bytes) -",
                    bg='black', fg=textFG).pack(side=tk.TOP)
# Input lebel
inputLebel = tk.Label(text="Input:", bg=appBG, fg=textFG).pack(pady=5)
# Incorrect lebel
incorrectLebel = tk.Label(text="RED length mismatch (not use)",
                          bg=appBG, fg='gray50').place(x=30, y=222)
# AOB Input box
inputAOB.pack(pady=5)

# Compare button
button = ttk.Button(app, text='Compare', command=printResult)
button.pack(pady=5)

# Result (Per Digit)
resultLebelDigit = ttk.Label(text='Result (Per Digit)').pack(pady=5)
outputResultDigit.pack()

# Result (Per Byte)
resultLebelByte = ttk.Label(text='Result (Per Byte)').pack(pady=5)
outputResultByte.pack()

# Mask Digit
maskDigitLebel = ttk.Label(text='Mask (Per Digit)').pack(pady=5)
outputMaskDigit.pack()

# Mask Byte
maskByteLebel = ttk.Label(text='Mask (Per Byte)').pack(pady=5)
outputMaskByte.pack()

# C Style
CstyleLebel = ttk.Label(text='C Style').pack(pady=5)
outputCstyle.pack()

# Pymem Style
PymemStyleLebel = ttk.Label(text='Pymem Style').pack(pady=5)
outputPymemStyle.pack()

# Footer
Footer = tk.Label(width="500", text="- click above output boxes for copy to clipboard -",
                  bg='black', fg=textFG)

# disable edit output box
outputResultDigit.configure(state='disabled')
outputResultByte.configure(state='disabled')
outputMaskDigit.configure(state='disabled')
outputMaskByte.configure(state='disabled')
outputCstyle.configure(state='disabled')
outputPymemStyle.configure(state='disabled')

# bind event mouse left click copy content to clipboard
outputResultByte.bind("<Button-1>", resultbyte_clip)
outputResultDigit.bind("<Button-1>", resultdigit_clip)
outputMaskDigit.bind("<Button-1>", maskdigit_clip)
outputMaskByte.bind("<Button-1>", maskbyte_clip)
outputCstyle.bind("<Button-1>", cstyle_clip)
outputPymemStyle.bind("<Button-1>", pymemstyle_clip)

Footer.pack(side=tk.BOTTOM)

# Refreshing footer text
Refresher()

app.mainloop()