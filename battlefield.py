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
        self.battle = ''
    def run_game(self,game):
        self.game = game
        print("The game begins")

    def display_welcome(self,welcome):
        self.welcome =welcome
        
    def battle_round(self):
        self.battle

    def add_robots_to_fleet(self):
        self.fleet.add_robots()


    def add_dinos_to_herd(self):
        self.herd.add_dinos()


        