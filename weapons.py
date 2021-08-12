#Class:Weapons
#Author: Samuel LP McKnight
#Created : August 11th, 2021

class Weapons:
#     ==== Consructor ====
    def __init__(self, name, atkpwr):
        self.weapon_name = name
        self.attack_power=atkpwr
#      ======Method=====
    def weapon_specs(self,name,attack_pwr):
#  === details of the weapons Robots will use ====
        self.weapon_name  = name
        self.attack_power = attack_pwr
    
