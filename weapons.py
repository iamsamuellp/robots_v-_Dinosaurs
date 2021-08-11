#Class:Weapons
#Author: Samuel LP McKnight
#Created : August 11th, 2021

class Weapons:
#     ==== Consructor ====
    def __init__(self,):
        self.weapon_name = ''
        self.attack_power= int
        self.weapon_type = True
#      ======Method=====
    def weapon_specs(self,name,attack_pwr):
#  === details of the weapons Robots will use ====
        self.weapon_name  = name
        self.attack_power = attack_pwr
        
        #  This Method is to determine if thew weapon is melee or not
    def type_weapon(self, type):
        if(self.melee_weapon ==  True):
           self.ranged_weapon =   False
        else:
           self.melee = True    
    # def type_weapon(self):
    #     if (self.melee == "melee"):
    #         print("robot has a melee Weapon")
    #     else:
    #         print("robot has a ranged Weapon")
