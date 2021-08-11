#Class:Fleet
#Author: Samuel LP McKnight
#Created : August 11th, 2021

from robots import Robots


class fleet: 
    def __init__(self,name, fleet,):
        self.name  = name 
        self.fleet = fleet
        self.robots = []

    # ===== Methods =====
    def add_robots(self):
        first_robot   = Robots("infantrybotI")
        second_robot  = Robots("GladitorI")
        third_robot   = Robots("infantrybotII")
        fourth_robot  = Robots("infantrybotIII")
        fifth_robot   = Robots("GladitorII")