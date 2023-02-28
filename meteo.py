#projet meteo
#récupération des valeurs météoroliques en fonction de la ville
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import requests, json

proxies = {"http":"http://agallard:mdp@172.30.137.29:3128"}

# votre clé API ici
api_key = "508a55426e3ba018a479effb47bf9b2c"

# URL de base
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def recupereMeteo(ville):
    # url de la requete
    url = base_url + "appid=" + api_key + "&q=" + ville+"&units=metric"
    print("l'url est",url)
    print("--------------------------------------------------")
    # methode get de la requete sur le site openweathermap
    response = requests.get(url,proxies=proxies)
    # response qui va être convertit en dictionnaire
    dict = response.json()
    print("données completes",dict)
    print()
    print(dict.keys())
    print("--------------------------------------------------")
    # récupère la clé main
    main = dict["main"]
    print("données de la clé main",main)
    print("--------------------------------------------------")
    #A compléter
    #lire la température
    temperature=dict["main"]["temp"]
    print("la température est",temperature)
    #lire la pression
    pression=dict["main"]["pressure"]
    print("la pression est ",pression)
    #lire l'humidité
    humidite=dict["main"]["humidity"]
    print("l'humidité est ",humidite)
    vent_vit=dict["wind"]["speed"]
    vent_deg=dict["wind"]["deg"]
    print("le vent a une vitesse de ",vent_vit," et un angle de",vent_deg)

    return (pression,temperature,humidite,vent_vit,vent_deg)

meteo=recupereMeteo("Le Mans")  #exécute la fonction gérant la requête GET
print("affichage du tuple", meteo) # affiche les 3 valeurs sous forme de tuple
print("pression",meteo[0]) # affiche la pression
print("temperature",meteo[1]) # affiche la température
print("humidite",meteo[2]) # affiche l'humidité
print("vitesse vent",meteo[3])
print("angle vent",meteo[4])

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('meteo2.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.comboBox_Ville.addItems(["Le Mans", "Lille", "Bayonne"])
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton_Maj.clicked.connect(self.boutonMaj)
        #Quand on clique sur le pushButtonAPropos, on appelle la méthode APropos
        self.pushButton_APropos.clicked.connect(self.APropos)
        self.show()             #affiche la fenêtre MainWindows

    def boutonMaj(self):
        print('bouton cliqué')
        #A compléter
        self.label_Temperature.setText('{0:.2f}°C'.format(meteo[1]))
        self.label_Pression.setText('{0:.2f}hPA'.format(meteo[0]))
        self.label_Humidite.setText('{0:.2f}%HR'.format(meteo[2]))
        self.label_vit_vent.setText('{0:.2f}km/h'.format(meteo[4]))
        self.label_deg_vent.setText('{0:.2f}°'.format(meteo[3]))


    def APropos(self):      #Gestion du message A Propos
        msg = QMessageBox()
        msg.setText("je sais pas quoi mettre là")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def paintEvent(self, event):    #Evènement paint pour afficher l'image de fond
        painter = QPainter(self)
        pic = QPixmap("logo.png")
        painter.drawPixmap(0,0, pic)

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()