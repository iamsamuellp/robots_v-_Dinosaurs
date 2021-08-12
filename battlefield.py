#Class:Battlefield
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from herd import Herd
from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet


class Battlefield: 
    def __init__(self, name):
        self.battlefield_name = name
        self.fleet = Fleet("Red Fleet")
        self.herd = Herd("Dino Horde 1")
        self.game=''     
        self.welcome =''
        self.battle()
    # ======= methods
    def run_game(self,game):
        self.game = game
        print("The game begins")

    def display_welcome(self,welcome):
        self.welcome =welcome
        print("Welcome to Robots versus Dinosaurs")

    def battle_round(self):

     while len(self.herd.add_dinos) >0 and len(self.fleet.add_robots) >0:
          choose= input("Choose your side: Dinos or Robots? ")
     if(choose == "Dinos"):
        Battlefield.dinos_move(self)
     elif (choose == 'robots'):
         Battlefield.robots_move(self)
         