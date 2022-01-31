import tkinter as tk
from tkinter.constants import S

window = tk.Tk()
window.title("Kalkulator")

class Kalkulator:
    def __init__(self,okno):
        self.dzialanieStringVar = tk.StringVar()  #equationStrVar
        self.wyrazenieString = "" #expressionStr
        self.Klawiatura = [
            ["7","8","9","+"],
            ["4","5","6","-"],
            ["1","2","3","*"],
            ["0","Clear","=","/"]
        ]
        self.GUI(okno)


    def GUI(self,okno):
        okno.geometry("260x200")
        self.PoleEkspresji = tk.Entry(okno,textvariable = self.dzialanieStringVar)
        self.PoleEkspresji.grid(columnspan=4,ipadx=60)

        RowIndex = 0
        while RowIndex <len(self.Klawiatura):
            calcRow = self.Klawiatura[RowIndex]

            columnIndex = 0
            while columnIndex < len(calcRow):
                buttonText = calcRow[columnIndex]
                #if buttonText == "Wyjscie":
                #    button = tk.Button(okno,text=buttonText, height=1,width=6, fg="black",bg="silver", command= lambda v=buttonText: self.buttonNacisk(v))
                #    button.grid(row = RowIndex+1, column=columnIndex, padx=4,columnspan=4)
                #    continue
                button = tk.Button(okno,text=buttonText, height=1,width=6, fg="black",bg="silver", command= lambda v=buttonText: self.buttonNacisk(v))
                button.grid(row = RowIndex+1, column=columnIndex)
                columnIndex += 1

            RowIndex += 1
        button = tk.Button(okno,text="Wyjscie", height=1,width=6, fg="black",bg="silver", command= lambda v="Wyjscie": self.buttonNacisk(v))
        button.grid(row = RowIndex+1, column=0,columnspan=4,sticky="EW")
        
    def buttonNacisk(self,wartosc):
        print("przycisk nacisniety: ",wartosc)
        
        if wartosc == "Clear":
            self.wyrazenieString = ""
            self.dzialanieStringVar.set("")
            return
        
        if wartosc == "=":
            wynik = str(eval(self.wyrazenieString))
            self.wyrazenieString = wynik
            self.dzialanieStringVar.set(wynik)
            return
        if wartosc =="Wyjscie":
            quit()
        
        self.wyrazenieString += str(wartosc)
        self.dzialanieStringVar.set(self.wyrazenieString)

kalkulator = Kalkulator(window)

window.mainloop()