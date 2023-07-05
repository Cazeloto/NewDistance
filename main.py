import os
import shutil
import time
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon
from PyQt6.QtCore import QCoreApplication
from ui_main import Ui_MainWindow
import sys
from qt_material import apply_stylesheet
import pandas as pd
import requests
import json
import urllib.parse


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SONDA DISTANCIAS")
        appIcon = QIcon(":/icons/_imgs/folder.png")
        self.setWindowIcon(appIcon)
        
        self.btn_saida.clicked.connect(self.open_path)
        self.btn_cidades.clicked.connect(self.open_file_cidade)      
        self.btn_bases.clicked.connect(self.open_file_bases)
        self.btn_bing.clicked.connect(self.open_file_bing)
        self.btn_processa.clicked.connect(self.processa)
   
    def open_path(self):        
        self.path =  QFileDialog.getExistingDirectory(self)                                                      
        self.txt_saida.setText(self.path) 
        
          
    def open_file_cidade(self):
        self.txt_cidades.setText(QFileDialog.getOpenFileName(self)[0]) 
    
    def open_file_bases(self):
        self.txt_bases.setText(QFileDialog.getOpenFileName(self)[0]) 
    
    def open_file_bing(self):
        self.txt_bing.setText(QFileDialog.getOpenFileName(self)[0])  
    
    def lblRefresh(self, ln):
        self.lbl_console.setText(ln)

           
        
    def processa(self):
        
        BingKeyFile = str(self.txt_bing.text())
        cidOrigem = str(self.txt_cidades.text())
        cidBase = str(self.txt_bases.text())
        pathDestino = str(self.txt_saida.text())
        
        with open(BingKeyFile, "r") as arquivo:
            bingKey = arquivo.read()
        
        arqOri = pd.read_excel(cidOrigem)
        arqDes = pd.read_excel(cidBase) 
    
        menorDist = 20000

        lenOri = len(arqOri)
        lenDes = len(arqDes)


        i = 0
        while lenOri > i:
            menorDist = 20000
            d = 0
            while lenDes > d:
                cidOri = arqOri['Cidade'][i]
                estOri = arqOri['Estado'][i]
                cidDes = arqDes['Cidade'][d]
                estDes = arqDes['Estado'][d]

                origem = urllib.parse.quote(cidOri + "," + estOri)
                destino = urllib.parse.quote(cidDes + "," + estDes)

                route = "http://dev.virtualearth.net/REST/v1/Routes?wayPoint.1=" + \
                    origem + "&wayPoint.2=" + destino + "&key=" + bingKey

                r = requests.get(route)
                if r.status_code != 200:
                    print(r.status_code)
                    cont = 0
                    while (r.status_code != 200) and (cont < 10):
                        cont = cont + 1
                        r = requests.get(route)
                        print(r.status_code)
                

                dt = json.loads(r.content)
                travelD = '%.2f' % (dt['resourceSets'][0]['resources'][0]['routeLegs'][0]['travelDistance'])

                travel = travelD.replace('.', ',')
                linha = cidOri + ";" + estOri + ";" + cidDes + ";" + estDes + ";" + travel + "\n"

                with open(pathDestino + "\distancias.csv", "a") as arquivo:
                    arquivo.write(linha)
                print(linha)
             
                self.lbl_console.setText(linha)
                self.lbl_cidade_status.setText("Total de Cidades - " + str(lenOri) + " / Processando - " + str(i+1) )
            
                
                QCoreApplication.processEvents()
              
                                
                
                d = d + 1

                if (float(travelD) < menorDist):
                    menorDist = float(travelD)
                    menorCid = cidDes
                    menorEst = estDes
                
                
              
            i = i + 1
            menDis = str(menorDist).replace('.', ',')
            linha2 = cidOri + ";" + estOri + ";" + menorCid + ";" + menorEst + ";" +str(menDis) + "\n"
           
            with open(pathDestino + "\menor_distancia.csv", "a") as arquivo:
                arquivo.write(linha2)

    
        self.lbl_console.setText("====== FIM DE PROCESSAMENTO =======")  
        QCoreApplication.processEvents()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    window.show()
    app.exec()