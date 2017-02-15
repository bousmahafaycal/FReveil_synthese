"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : 2017_2_13
Nom initial du module : synthese

"""
from synthese import *
from config import *

def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	print(" arguments : "+str(arguments))
	if len(arguments) != 0:
		print("dans le if")
		a = Synthese()
		for i in range(0,len(arguments)):
			a.synthese(arguments[i]);


start(["Testt"])