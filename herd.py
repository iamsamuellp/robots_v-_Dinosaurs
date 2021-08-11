#Class:Herd
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from dinosaurs import Dinosaurs


class herd:
    #  Constuctors
    def __init__(self, name):
        self.name = name
        self.dinos = []
    #  Methods
    def add_dinos(self):
        first_dino = Dinosaurs("Deinonychus")
        second_dino = Dinosaurs("dilophosaurusI")
        third_dino = Dinosaurs("Deinonychus")
        fourth_dino = Dinosaurs("Trex")
        fifth_dino = Dinosaurs("dilophosaurusII")
        self.dinos.append(first_dino)
        self.dinos.append(second_dino)
        self.dinos.append(third_dino)
        self.dinos.append(fourth_dino)
        self.dinos.append(fifth_dino)