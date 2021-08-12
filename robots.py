#Class:Weapons
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from weapons import Weapons


class Robots:
    # ======= Constructor========
    def __init__(self):
        self.robot_name = ''
        self.robot_health   = 0
        self.weapon     = Weapons("Rail Gun", 45)


# ======= Methods =======
    def robots_spec(self, name, health, attack):
        self.robot_name    = name
        self.robot_health  = health
        self.weapon        = attack

    def attack(self, dino):
        dino.health-=self.weapon.attack   

