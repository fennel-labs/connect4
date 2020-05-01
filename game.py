from connect4.field import Field
from connect4.drawer import Drawer

f = Field()
p = Drawer(f)

player = Field.Player.P1
game_ended = False

def callbackClick(column_number):
    global game_ended
    # check if game has not ended
    if game_ended:
        return
    # only mark player as done if there is no success
    try:
        if f.place(column_number):
            # chip was placed, so update field, evaluate and switch player
            p.drawBoard()
            # evaluate
            result = f.check()
            if result == Field.Player.P1:
                p.showMessage('Player 1 won!')
                game_ended = True
                return
            elif result == Field.Player.P2:
                p.showMessage('Player 2 won!')
                game_ended = True
                return
            # switch player
            player = f.switchPlayer()
            if player == Field.Player.P1:
                p.showMessage("Player 1 is playing...")
            elif player == Field.Player.P2:
                p.showMessage("Player 2 is playing...")
        else:
            p.showMessage('Bin is already full. Try again.')
    except:
        p.showMessage('You failed to click a bin. Try again.')

import matplotlib.pyplot as plt

if __name__ == '__main__':
    p.setCallback(callbackClick)
    p.showMessage('Player 1 is playing...')
    p.drawBoard()
    plt.show(block=True)

    
    