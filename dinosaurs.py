#Class:Dinosaurs
#Author: Samuel LP McKnight
#Created : August 11th, 2021

class Dinosaurs:
    # ======= Constuctor ===========
    def __init__(self):
        self.dino_name = ''
        self.dino_attack = ''
        self.dino_health = 0

    # Methods =============
    def dino_specs(self, breed, attack, health):
        # specifactions of dinosuars
        self.dino_name    = breed 
        self.dino_attack  = attack
        self.dino_health  = health 