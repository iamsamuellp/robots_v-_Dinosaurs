#Class:Herd
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from dinosaurs import Dinosaurs


class herd:
    #  Constuctors
    def __init__(self, name):
        self.name = name
        self,dinos = []
    #  Methods
    def add_dinos(self):
        first_dino  = Dinosaurs("")
        second_dino = Dinosaurs("")
        third_dino = Dinosaurs("")
        fourth_dino = Dinosaurs("")
        fifth_dino = Dinosaurs("")