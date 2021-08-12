#Class:Dinosaurs
#Author: Samuel LP McKnight
#Created : August 11th, 2021

class Dinosaurs:
    # ======= Constuctor ===========
    def __init__(self):
        self.dino_name = ''
        self.dino_attack = 0
        self.dino_health = 0

    # Methods =============
    def dino_specs(self, breed, atk, health):
        # specifactions of dinosuars
        self.dino_name    = breed 
        self.dino_attack  = atk
        self.dino_health  = health 
    
    def dino_hit(self,bot):
        bot.health -=self.atk    

    