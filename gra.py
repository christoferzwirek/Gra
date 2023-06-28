import sys
#import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout
import random
import pandas as pd
#import pydoc 
#
""" 
Autor 
Radosław Wirkus

Nazwa
Zgadywanie liczb
Opis 
Zgadywanie liczby całkowitej od 1 do 100

"""
#liczba=71
liczba = random.randint(1, 100)
#global losowanie
losowanie =1
#global C
C=0
trafiony = 0
ile = 0
ilew=0

tryb=0




class MyApp(QWidget):
    
    def __init__(self):
        """
        interfejs
        """
        super().__init__()
        self.window_width, self.window_height = 1600, 150
        self.setMinimumSize(self.window_width, self.window_height)

        self.setWindowTitle('Command Line App')
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.kod = []
        
        self.editorOutput = QPlainTextEdit()
        layout.addWidget(self.editorOutput, 7)
        
        self.editorCommand = QPlainTextEdit()
        layout.addWidget(self.editorCommand, 1)

       

        buttonLayout = QHBoxLayout()
        layout.addLayout(buttonLayout)

        self.button_run = QPushButton('&start', clicked=self.runCommand)
        buttonLayout.addWidget(self.button_run)

        self.button_clear = QPushButton('enter' )
        self.button_clear.clicked.connect(self.enter)
        buttonLayout.addWidget(self.button_clear)

        self.button_clearq = QPushButton('&Clear', clicked=lambda: self.editorOutput.clear())
        buttonLayout.addWidget(self.button_clearq)
        #self.editorCommand.insertPlainText('dir')

    def wypisz_punktacje(self,lista):
        """ 
        wypisanie punktacji z listy
        """
        lista_rozdzielona=[]
        for i in lista:
            lista_rozdzielona.append(i.split(":"))
        li=pd.DataFrame(lista_rozdzielona)
        li = li.sort_values(by = 1 , axis=0, ascending=False, inplace=False, kind='quicksort', na_position='first')
        self.editorOutput.appendPlainText(str(li))
        print(li)

    def wygrana(self,gracz, tryb, ilew):
       # global tryb
        #tu obliczenie średniej i dodanie do pliku
        """ 
        Funkcja do zapisu do pliku.Obliczanie punktacji. Wywietlanie wyniku
        
        """
        print("gracz: "+str(tryb)+"1")
        punkty=0
        if ilew>100:
            print("Nie graj dalej, jesteś za słaby... ")
        else:
            punkty = (1/(ilew))*100
    
        plik = open(str('wyniki')+str(tryb)+'.txt', 'a+')
        jest=0
        for linia in plik:
            linia=linia.split(':')
            if linia[0]==gracz:
               srednia=(float(linia[1][:-1])+punkty)/2
               jest=1
        if jest==0:
            srednia=punkty
    
        plik.close()  
        #----
        lista=[]
       
        plik = open(str('wyniki')+str(tryb)+'.txt', 'r').read()
        linia=plik.split('\n') 
       
        userdl = len(gracz)+1
    
        for i in linia:
            lista.append(i)
           
    
        for j in range(len(lista)):
            a=lista[j]
            if str(gracz+":") == a[:userdl]:
                niema=1
                a = str(gracz)+str(':')+str(srednia)
                lista[j]=a
                break
            else:
                niema=0
        if niema==0:
            a = str(gracz)+str(':')+str(srednia)
            lista.append(a)
        #Wypisywanie dla użytkownika
        wynik=round(srednia,2)
        self.editorOutput.appendPlainText(str("Zdobyłeś "+str(wynik)+" puktów. "))
        print("Zdobyłeś "+str(wynik)+" puktów. ")
       
        plikz = open(str('wyniki')+str(tryb)+'.txt', 'w')
        for k in range(len(lista)):
            if k == len(lista)-1:
                plikz.write(lista[k])
            else:
                plikz.write(lista[k] + str('\n'))
        plikz.close()
        ##Ogólna punktacja
        self.editorOutput.appendPlainText(str(lista))
        print(lista)
        self.wypisz_punktacje(lista)

    def runCommand(self):
        """Start"""
        self.editorOutput.appendPlainText(str("Zagramy w zgadywanie liczb\n"))
        self.editorOutput.appendPlainText(str("Tryby: 1-łatwy, 2-normalny, 3-trudny."))
        self.button_run.disconnect()
        #liczba1 = int(self.editorCommand.toPlainText())#pobranie
        #self.editorOutput.appendPlainText(str(liczba1))
        #print("Tryby: 1-łatwy, 2-normalny, 3-trudny.")
    def enter(self,zmienna):
        
        """
   podawanie trybu trudności
    
    """
        layout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        layout.addLayout(buttonLayout)

        zmienna2 = self.editorCommand.toPlainText()#pobranie   
       # self.editorOutput.appendPlainText(str(zmienna))
       # zmienna+=1
       
      #  print(tryb)
        self.inna(zmienna2)
    def inna(self,tryb2):
        global nazwapliku
        global tr,proby,tryb
        
       # print(type(tryb))
        global C
        if C==0:
            """
            sprawdzanie trybu trudnoci
            """
            tryb=int(tryb2)
            if int(tryb)==1:
                self.editorOutput.clear()
                self.editorCommand.clear()
                self.editorOutput.appendPlainText(str("Podaj swoją nazwę: "))
                #self.button_clear = QPushButton('enter2', clicked=self.enter2)
                #buttonLayout.addWidget(self.button_clear)
                #self.kod.pop().deleteLater()
                self.button_clear.clicked.connect(self.enter2)
                nazwapliku='tryb1.txt'
                tr = 'łatwy'
                C=1
                proby=100
               
                
            elif int(tryb)==2:
                self.editorOutput.clear()
                self.editorCommand.clear()
                self.editorOutput.appendPlainText(str("Podaj swoją nazwę: "))
                self.button_clear.clicked.connect(self.enter2)
                nazwapliku='tryb2.txt'
                tr='normalny'
                C=1
                proby=10
            elif int(tryb)==3:
                self.editorOutput.clear()
                self.editorCommand.clear()
                self.editorOutput.appendPlainText(str("Podaj swoją nazwę: "))
                self.button_clear.clicked.connect(self.enter2)
                nazwapliku='tryb3.txt'
                tr='trudny'
                C=1
                proby=5
            else:
               self.editorOutput.appendPlainText(str("zły wybór"))
           
    def enter2(self):
        plik = open(nazwapliku, 'a+')
        global C
        global trafiony,ile,ilew,proby,liczba,losowanie
        global tryb,gracz
        #gracz=""
        if C==1:
           """
           zapisywanie nazwy gracza do pliku
           """
           zmienna = self.editorCommand.toPlainText()#pobranie   
           gracz=str(zmienna)
          # print(gracz)
       # self.editorOutput.appendPlainText(str(zmienna))
           plik.write("\nGracz: "+str(zmienna)+"\nTryb: "+tr+"\nLosowanie: "+str(losowanie)+"\nLiczba: "+str(liczba)+'\nPróby: ')
           
           self.editorOutput.clear()
           self.editorCommand.clear()
           self.editorOutput.appendPlainText(str("----------Zacząłeś grę----------\n"))
           #traf=-1
        if C==2:
            #while(trafiony!=1):
            """
            gra
            """
            ile+=1
            ilew+=1
            #pydoc
            self.editorOutput.appendPlainText(str("\nZgadnij liczbę: "))
            traf=int(self.editorCommand.toPlainText())
            plik.write(str(traf)+" ")
            if traf<liczba:
                self.editorOutput.appendPlainText(str("Za mała\n"))
                trafiony=0
            elif traf>liczba:
                self.editorOutput.appendPlainText(str("Za duża\n"))
                trafiony=0
            
            
           # print("traf: "+str(traf))
            #print("liczba: "+str(liczba))
            print("ile: "+str(ile))
            print("próby: "+str(proby))
            if ile==proby and trafiony==0:
                """
                nie udana próba
                """
                ile=0
                self.editorOutput.appendPlainText(str("Nie udało Ci się "+str(proby)+" razy, nowa liczba ;)\nPoprzednią była "+str(liczba)+"\n"))
                #print("Nie udało Ci się "+str(proby)+" razy, nowa liczba ;)\nPoprzednią była "+str(liczba)+"\n")
                liczba = random.randint(1, 100)
                losowanie+=1
                plik.write("\nLosowanie: "+str(losowanie)+"\nLiczba: "+str(liczba)+'\nPróby: ')
            
            #-----------------
        
        
            if traf==liczba:
                """
                wypisanie statyskyk
                """
                self.editorOutput.clear()
                self.editorOutput.appendPlainText(str("Wygrałeś! - trafiłeś za "+ str(ile)+", ale razem podjąłeś "+str(ilew)+" prób"))
                print("Wygrałeś! - trafiłeś za "+ str(ile)+", ale razem podjąłeś "+str(ilew)+" prób")
                trafiony=1
                self.editorOutput.appendPlainText(str("----------------------------------\n------------STATYSTYKI------------\n----------------------------------\n"))
                print("----------------------------------\n")
                print("------------STATYSTYKI------------\n")
                print("----------------------------------\n")
                print(gracz)
                self.wygrana(gracz, tryb, ilew)
           
        plik.close()
        C=2
        
        
"""
main
"""
if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

