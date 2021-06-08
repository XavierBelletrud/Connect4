import numpy as np

class Gamer():

    
    """
    attributs : identification, couleur, nom ou numéro 1 et -1
    methode : faire un choix de colonne

    
    
    joueur_humain(joueur)
    faire un choix de colonne(input)

    joueur_bot(joueur)
    faire un choix de colonne, 2 choix : random ou IA
    """

    def __init__(self):
        self.numero = numero
        self.couleur = couleur
        # self.choice = choice


    def nbPlayer(self):
        """
        DOCSTRING: number of player(s)
        """
        while self.numberOfPlayer <= 0 or self.numberOfPlayer > 2:
            self.numberOfPlayer = int(input("Select number of player(s) 1 or 2 :"))
        return print("\n", f"The game will begin with {self.numberOfPlayer} player(s)", "\n")

    def choicePlay(self):
            choice = int(input('Choice your game: \n 1: Player1 Vs Player2 \n 2: Player1 VS Bot \n 3: Bot VS Bot \n'))
            return choice

class HumanGamer(Gamer):

    def input_humain():
        choice = int(input('Select a number between 0 and 6'))
        return choice 

class CPUGamer(Gamer):
    
    def input_CPU():
        choice = np.random.randint(0, 7) # random player choice
        return choice 







class Board():
    """
    objets : joueurs,  interface d'affichage 
    attribut : plateau, type de joueur
    methode : vérification ligne, colonne, diagonale ; player_input ; global_player(42 coups)

    Principe de gravité (les colonnes se remplissent)


    is_board_full
    is_col_full

    """

    def __init__(self):
        self.nblines_int = 6
        self.nbcolumns_int = 7
        self.board = np.zeros((self.nblines_int, self.nbcolumns_int), dtype=int)

    def displayBoard(self):
    """
    DOCSTRING: Display the board
    """
        board = self.board
        return print(board, "\n")

    def isColFull(self, column:int):
        if 0 not in self.board[:,column]:
        return True
        else:
        return False

    def colChoice(self, player:int, choice:int):
    """
    DOCSTRING: Inserting a coin into a col
    """
    
        if self.isBoardFull():
        return -2
        elif self.isColFull(choice):
        print(f'Column {choice} full')
        return -1
        else:
        column = self.board[:,choice]
        for i in range(0, self.default_nboflines)[::-1]:
            if column[i] == 0:
            column[i] = player
            break
        return i


    def isBoardFull(self):
    """
    DOCSTRING: 
    """
        return 0 not in self.board[0]



    def a_toi_de_jouer(self, player, choice):
      """
      DOCSTRING: 
      """
      
        line = self.colChoice(player, choice) # Shall we play ?
        if line < 0:
            return line
        
        # Connect4 test on col
        column = self.board[:,choice]
        if np.all(column[line:line+4] == player) and len(column[line:line+4]) == 4:
            return self.board, 1, True
    
        # Connect4 test on line
        window = [player] * 4
        test = np.convolve(self.board[line, max(0, choice-3):choice+4], window)
        if player*4 in test:
            return self.board, 1, True #2
        
        # Connect4 test on diag
        board_padded = np.pad(self.board, (3, 3))
        #m8 = self.board[max(0, line-4):line+4, max(0, choice-4):choice+4]
        m8 = board_padded[line-3+3:line+4+3, choice-3+3:choice+4+3]
    
        d1 = np.diag(m8)
        d2 = np.diag(m8[::-1])
      
      #
        test = np.convolve(d1, window)
        if player*4 in test:
            return self.board, 1, True #3
        
        #
        test = np.convolve(d2, window)
        if player*4 in test:
            return self.board, 1, True
    


class Interface():
    """ terminal et graphique """
    pass




if __name__ == "__main__":
    B = Board()
    B.displayBoard() 

############################################################################################################







 

  

  

  

  



      

    # Random move for player2
    choice2 = np.random.randint(0, 7) # random player choice

    player2 = -player

    line = self.colChoice(player2, choice2)
    while line == -1: # if the line is full....
      line = self.colChoice(player2, choice2)
    if line == -2:
      return self.board, 0, True # Draw
    
    # Connect4 test on col
    column = self.board[:,choice2]
    if np.all(column[line:line+4] == player2) and len(column[line:line+4]) == 4:
      return self.board, -1, True
    # Connect4 test on line
    window = [player2] * 4
    test = np.convolve(self.board[line, max(0, choice2-3):choice2+4], window)
    if player2*4 in test:
      return self.board, -1, True
    
    # Connect4 test on diag
    board_padded = np.pad(self.board, (3, 3))
    m8 = board_padded[line-3+3:line+4+3, choice2-3+3:choice2+4+3]
    d1 = np.diag(m8)
    d2 = np.diag(m8[::-1])
    #
    test = np.convolve(d1, window)
    if player2*4 in test:
      return self.board, -1, True
    #
    test = np.convolve(d2, window)
    if player2*4 in test:
      return self.board, -1, True

    return self.board, 0, self.isBoardFull()

    # while (p1 <= 1) or (p1 > 7):
    #   p1 = int(input("Player 1 : Choose an empty column between (1 to 7) "))
    # return print(f"Player 1 chose {p1}")

g = Pyfour()

#g.nbPlayer()
g.displayBoardNumber()
g.displayBoard()
#for i in range(0, 6): print(g.board[[i]])
#g.colChoice()

g.colChoice()

g.displayBoard
#g.createBoard()
#g.displayBoard()

g = Pyfour()

print(g.player_input(player= 1, choice=3))

g.player_input(player= 1, choice=5)

g.displayBoard
