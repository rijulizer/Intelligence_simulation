import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse

from env import Environment

class Agent:
    
    def __init__(self, energy, pos_x, pos_y, angle=0.0,):
        self.energy = energy
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = 3.0 # height
        self.width = 1.0 # width
        self.angle = angle # inital orientation
        self.env_size = 50

    def move_forward(self, move_unit=1):
        """
        moves the body forward in the direction of the orientation
        """
        # as the angle is anticlock wise adjust the x,y movememnt
        angle = 90 + self.angle # offset angle
        angle_c = 2 * np.pi / 360
        self.pos_x += move_unit * np.cos(angle_c * angle)
        self.pos_y += move_unit * np.sin(angle_c * angle)
         
    
    def move_rotate(self, roate_unit = 30):
        self.angle += roate_unit # rotate anticlock wise

#     def sense_env(self,):
#         """
#         Gets envromental information of the agents current location
#         """
    def draw(self):
        
        # create body
        fig, ax = plt.subplots()

        # define body shape
        self.body = Ellipse((self.pos_x, self.pos_y), self.width, self.height, angle = self.angle, facecolor='lightblue', edgecolor='blue')
        ax.add_patch(self.body)
        # for i in range(n):

            # Display the plot with a delay
            # plt.pause(2)  # Adjust the delay time as needed
            
            # Clear the previous contour before drawing the next one
        # Set axis limits
        ax.set_xlim(0, self.env_size+2)
        ax.set_ylim(0, self.env_size+2)
        
        plt.show()
    
    def simulate(self, iter):
        
        # create body
        fig, ax = plt.subplots()
        # Set axis limits
        ax.set_xlim(0, self.env_size+2)
        ax.set_ylim(0, self.env_size+2)
        for i in range(iter):
            # define body shape
            self.body = Ellipse((self.pos_x, self.pos_y), self.width, self.height, angle = self.angle, facecolor='lightblue', edgecolor='blue')
            ax.add_patch(self.body)
            # Display the plot with a delay
            plt.pause(1)  # Adjust the delay time as needed
            # Clear the previous contour before drawing the next one
            self.body.remove()
            self.move_forward(1)
            if i % 5 == 0:
              self.move_rotate()
        
        
        plt.show()



if __name__ == "__main__":
    agent = Agent(energy=150, pos_x=30, pos_y=20, angle=30)
    # # agent.draw()
    agent.simulate(15)