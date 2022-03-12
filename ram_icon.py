# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:15:25 2022

@author: user
"""
# Import the required libraries
from pystray import MenuItem as item
from pystray import Icon
from PIL import Image, ImageDraw, ImageFont
from psutil import virtual_memory
from time import sleep


# functions

#to update image of icon
def update_image(icon, msg):   
    
    #defualts
    icon_color = "#00CA4E"
    med_color = "#FFBD44"
    high_color =  "#FF605C"
    
    #color logic
    if(msg>60):
        icon_color=med_color
    if(msg>80):
        icon_color = high_color
    
    #create the icon
    W, H = (700,700)
    im = Image.new("RGBA",(W,H),"#101010")
    draw = ImageDraw.Draw(im)
    X, Y = 350, 350
    r = 350
    draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill = icon_color, outline =icon_color)
    
    #save image
    im.save("icon_image.png", "PNG")
    
    #update icon
    icon.icon = Image.open("icon_image.png")


# change ui periodically
def change_ui(icon):
    icon.visible = True
    
    old_msg = -1
    while(True):
        
        #ram stats
        msg = int(virtual_memory().percent)
        
        if msg != old_msg:    
            #update the image
            update_image(icon, msg)
        
        #update old_msg
        old_msg = msg
        
        #do it each second
        sleep(1)
    
#classes
class Icon_class():
    def __init__(self):
        #open image
        self.image = Image.open("icon_image.png")
        
        #create icon
        self.icon=Icon("name", self.image, "ram level", ())
        
    def run_icon(self):
        #run icon
        self.icon.run_detached(setup = change_ui)

#main
if __name__ == "__main__":
    #create icon object
    ram_icon = Icon_class()
    
    #run icon
    ram_icon.run_icon()
