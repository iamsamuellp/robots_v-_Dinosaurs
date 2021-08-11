#Class:Weapons
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from weapons import Weapons


class Robots:
    # ======= Constructor========
    def __init__(self):
        self.robot_name = ''
        self.robot_rank = ''
        self.robot_health    = int
        self.weapon     = Weapons


# ======= Methods =======
    def robots_spec(self, name, health, rank):
        self.robot_name    = name
        self.robot_health  = health
        self.robot_rank    = rank   
        
