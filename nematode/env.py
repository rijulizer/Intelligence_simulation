import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

class Environment:
    """
    A class that creates a square box as the enviroment and can add various aspects to the environment
    """
    
    def __init__(self, size, ):
        self.size = size
        
        # keep trak of all the information of env but dont reveal it to the agents, agents only get to know the information of a particular location they are in
        self.env_info = {
            'size': size,
        }
    
    def get_info(self, pos_x, pos_y):
        """
        returns the information on that particlular location, information may include source of food, heat etc
        """
        
        return None
    
    def drop_food(self, loc=None):
        """
        Adds a food source in the location provided
        """
        self.food_loc = loc
        self.env_info['food_loc'] = loc


        # radilly dispense smell of food, smell =1 at the source and deceases radially 

    def radial_decay(self, x, y, sigma):
        # radial distance 
        r = np.sqrt(x**2 + y**2)
        # 2D gaussian function
        value = np.exp(-r**2 / (2 * sigma**2))
        return value


    def drop_heat(self, loc=None):
        """
        Adds a food source in the location provided
        """
        pass


    def draw_env(self):
        fig, ax = plt.subplots()
        ax.add_patch(Rectangle((1,1),self.size ,self.size, linewidth=2.0, edgecolor='r', facecolor='white'))
        
        if self.food_loc:
            # create a grid of x,y values
            x = np.linspace(1, self.size+1, 100)
            y = np.linspace(1, self.size+1, 100)

            # create a mesh grid
            X, Y = np.meshgrid(x,y)
            # calcualte the value for each point in the grid
            val = self.radial_decay(X- self.food_loc[0], Y- self.food_loc[1], sigma=1)

            contour = ax.contourf(X, Y, val, cmap='magma')
            fig.colorbar(contour, ax=ax, label='dispensed smell')
        
        
        # Set axis limits
        ax.set_xlim(0, self.size+2)
        ax.set_ylim(0, self.size+2)
        
        plt.show()
    
    def env_simulate(self,n):
        """
        Simulates env: drops food and other objects in random locations
        inpus: n number of simulations
        """
        # draw the enviroment in simulation
        fig, ax = plt.subplots()
        ax.add_patch(Rectangle((1,1), self.size ,self.size, linewidth=2.0, edgecolor='r', facecolor='white'))

        for i in range(n):
            # get random locations
            x = np.random.randint(1, self.size+1)
            y = np.random.randint(1, self.size+1)
            # drop food in the random location in the enviroment
            self.drop_food((x,y))

            # create a grid of x,y values
            x = np.linspace(1, self.size+1, 100)
            y = np.linspace(1, self.size+1, 100)

            # create a mesh grid
            X, Y = np.meshgrid(x,y)
            # calcualte the value for each point in the grid
            val = self.radial_decay(X- self.food_loc[0], Y- self.food_loc[1], sigma=1)

            contour = ax.contourf(X, Y, val, cmap='magma')
            # fig.colorbar(contour, ax=ax) #, label='dispensed smell'
            # Display the plot with a delay
            plt.pause(2)  # Adjust the delay time as needed
            
            # Clear the previous contour before drawing the next one
            for c in contour.collections:
                c.remove()
        
        
        # Set axis limits
        ax.set_xlim(0, self.size+2)
        ax.set_ylim(0, self.size+2)
        
        plt.show()
        

if __name__ == "__main__":
    env = Environment(10)
    # manually drop food in a location
    env.drop_food((3,5))
    env.draw_env()
    # or simulate the food dropping
    # env.env_simulate(10)


