import matplotlib.pyplot as plt
import numpy as np
from field import Field

class Drawer:

    RADIUS = 0.4

    def __init__(self, field):
        self.field = field

        # create and adjust axes
        self.fig, self.ax = plt.subplots()
        self.ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        self.ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
        self.ax.set_aspect('equal')

        # register callback to figure
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def drawBoard(self):

        # reset axes first
        self.ax.clear()
        self.ax.set_xlim(-0.5, Field.WIDTH-0.5)
        self.ax.set_ylim(-0.5, Field.HEIGHT-0.5)

        dim = self.field.grid.shape

        for row in range(0,dim[0]):
            for col in range(0,dim[1]):
                player = self.field.grid[row, col]
                if player == 0:
                    color = 'white'
                elif player == Field.Player.P1:
                    color = 'red'
                elif player == Field.Player.P2:
                    color = 'yellow'
                
                circle = plt.Circle((col, row), self.RADIUS, facecolor=color, edgecolor='k')
                self.ax.add_artist(circle)


    def onclick(self, event):
        column_number = -1
        x_coord = event.xdata
        y_coord = event.ydata

        if x_coord != None and y_coord != None:
            if y_coord >= 0-Drawer.RADIUS and y_coord <= Field.HEIGHT+Drawer.RADIUS:
                if x_coord >= 0-Drawer.RADIUS and x_coord <= Field.WIDTH+Drawer.RADIUS:
                    column_number = int(round(x_coord))

        #print("Clicked on {}".format(column_number))
        return column_number
    

if __name__ == '__main__':
    f = Field()
    p = Drawer(f)
    f.place(0, Field.Player.P1)
    f.place(1, Field.Player.P2)
    f.place(1, Field.Player.P1)
    p.drawBoard()
    plt.show()
    