#Class:Herd
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from dinosaurs import Dinosaurs


class Herd:
    #  Constuctors
    def __init__(self, name):
        self.name = name
        self.dinos = []
    #  Methods
    def add_dinos(self):
        first_dino = Dinosaurs("Deinonychus", 40, 40 )
        second_dino = Dinosaurs("dilophosaurusI", 60, 50)
        third_dino = Dinosaurs("Deinonychus", 40, 40  )
        fourth_dino = Dinosaurs("Trex", 100, 60)
        fifth_dino = Dinosaurs("dilophosaurusII", 60, 50)

        self.dinos.append(first_dino)
        self.dinos.append(second_dino)
        self.dinos.append(third_dino)
        self.dinos.append(fourth_dino)
        self.dinos.append(fifth_dino)