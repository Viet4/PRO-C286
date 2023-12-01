from controller import Robot
from controller import Keyboard
import random

robot = Robot()
keyboard = Keyboard()

timestep=64

wheel1=robot.getDevice("wheel1")
wheel1.setPosition(float('inf'))
wheel1.setVelocity(0.0)

wheel2=robot.getDevice("wheel2")
wheel2.setPosition(float('inf'))
wheel2.setVelocity(0.0)

wheel3=robot.getDevice("wheel3")
wheel3.setPosition(float('inf'))
wheel3.setVelocity(0.0)

wheel4=robot.getDevice("wheel4")
wheel4.setPosition(float('inf'))
wheel4.setVelocity(0.0)

ds_1=robot.getDevice("ds_1")
ds_2=robot.getDevice("ds_2")

speed=4
 
keyboard.enable(timestep)
ds_1.enable(timestep)
ds_2.enable(timestep)

automode = True
key_pressed = -1

num_of_turns = 0
while (robot.step(timestep) !=-1):
    prev_key = key_pressed
    key_pressed= keyboard.getKey()
    # print(key_pressed)
    
    if key_pressed == 65 and prev_key == -1:
        automode = not automode
    
    
    if (automode):
        ds_1_value = ds_1.getValue()
        ds_2_value = ds_2.getValue()
        print(ds_1_value)
        print(ds_2_value)
    
        if ds_1_value < 1000 or ds_2_value < 1000:
            num_of_turns = 8
    
        if num_of_turns == 0:
            random_direction = random.choice([0,1])

        if (num_of_turns > 0):
            num_of_turns = num_of_turns -1

            if(random_direction == 0):
                wheel1.setVelocity (-speed)
                wheel2.setVelocity (speed) 
                wheel3.setVelocity(-speed)
                wheel4.setVelocity(speed)
            elif (random_direction == 1):
                wheel1.setVelocity(speed)
                wheel2.setVelocity(-speed)
                wheel3.setVelocity(speed) 
                wheel4.setVelocity(-speed)
        else:
                wheel1.setVelocity(speed)
                wheel2.setVelocity(speed)
                wheel3.setVelocity(speed)
                wheel4.setVelocity(speed)
        
    else:
        wheel1.setVelocity(speed)
        wheel2.setVelocity(speed)
        wheel3.setVelocity(speed)
        wheel4.setVelocity(speed)
    
        # front movement - press up arrow key
        if(key_pressed== 315):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
            
        # back movement - press down arrow key   
        if(key_pressed== 317):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(-speed)
        
        # left movement - press left arrow key      
        if(key_pressed== 314):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(speed)
        
        # right movement - press right arrow key     
        if(key_pressed== 316):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(-speed)
        
        # if no key is pressed   
        if(key_pressed== -1):
            wheel1.setVelocity(0)
            wheel2.setVelocity(0)
            wheel3.setVelocity(0)
            wheel4.setVelocity(0)