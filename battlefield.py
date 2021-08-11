#Class:Battlefield
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from dinosaurs import Dinosaurs
from fleet import Fleet


class Battlefield: 
    def __init__(self, name):
        self.battlefield_name = name
        self.fleet = Fleet("Red Fleet")
        self.dinos = Dinosaurs("Dino Horde 1")





    def add_robots_to_fleet(self):
        self.fleet.add_robots()





    def battle_round():
        