import random


class gameNode:
    def __init__(self, number, player1Pts, player2Pts, currentPlayer, left, right, heuristicValue, dynamicValue):      # player1Pts = player, player2Pts = computer
        self.number = number            # player1Pts | num | player2Pts
        self.player1Pts = player1Pts    #  0 | 999 | 0
        self.player2Pts = player2Pts                                                
        self.currentPlayer = currentPlayer    
        self.left = left   # Virsotne                                       
        self.right = right 
        self.heuristicValue = heuristicValue
        self.dynamicValue = dynamicValue
        



class gameTree:
    def __init__(self, number):
        self.root = self.build(gameNode(number, 0, 0, "player", None, None, 0, -6000), 1)
        self.print_tree(self.root)
    

    def build(self, node, num):
        gameList = ["player","computer"]
        nt = gameList[num]

        if (node.number >= 10):
            if (num == 0):
                num = 1
                if(node.number % 2 == 0):
                    heuristicValue = node.player1Pts - node.player2Pts + 0
                    node.right = gameNode(node.number//2, node.player1Pts+2, node.player2Pts, nt, None, None, heuristicValue, -6000)
                    self.build(node.right, num)

                if(node.number % 3 == 0):
                    heuristicValue = node.player1Pts - node.player2Pts + 2
                    node.left = gameNode(node.number//3, node.player1Pts, node.player2Pts+3, nt, None, None, heuristicValue, -6000)
                    self.build(node.left, num)

            else:
                num = 0
                if(node.number % 2 == 0):
                    heuristicValue = node.player1Pts - node.player2Pts + 0
                    node.right = gameNode(node.number//2, node.player1Pts, node.player2Pts+2, nt, None, None, heuristicValue, -6000)
                    self.build(node.right, num)

                if(node.number % 3 == 0):
                    heuristicValue = node.player1Pts - node.player2Pts + 2
                    node.left = gameNode(node.number//3, node.player1Pts+3, node.player2Pts, nt, None, None, heuristicValue, -6000)
                    self.build(node.left, num)
            
            return node
    

    # --- CHAT GPT
    def print_tree(self, node, level=0): 
        #"""
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.number, node.currentPlayer, node.player1Pts, node.player2Pts, node.heuristicValue)
            self.print_tree(node.left, level + 1)
        #"""
     # --- CHAT GPT


# Nemts no interneta video
def minimax(ntraversedNodes, node, depth, isMaximisingPlayer):
    if (depth == 0 or ((node.left == None and node.right == None))):
        node.dynamicValue = node.heuristicValue
        return ntraversedNodes, node.heuristicValue
    
    
    if isMaximisingPlayer:
        maxEval = -10000
        if (node.left != None):
            ntraversedNodes, eval = minimax(ntraversedNodes, node.left, depth - 1, False)
            maxEval = max(maxEval, eval)
            ntraversedNodes+=1
        
        if (node.right != None):
            ntraversedNodes,eval = minimax(ntraversedNodes, node.right, depth - 1, False)
            maxEval = max(maxEval, eval)
            ntraversedNodes+=1


        node.dynamicValue = maxEval
        return ntraversedNodes, maxEval
    
    else:
        minEval = 10000
        if (node.left != None):
            ntraversedNodes, eval = minimax(ntraversedNodes,node.left, depth - 1, True)
            minEval = min(minEval, eval)
            ntraversedNodes+=1
        
        if (node.right != None):
            ntraversedNodes, eval = minimax(ntraversedNodes,node.right, depth - 1, True)
            minEval = min(minEval, eval)
            ntraversedNodes+=1


        node.dynamicValue = minEval
        return ntraversedNodes, minEval
    

def alphaBeta(ntraversedNodes, node, depth, isMaximisingPlayer, alpha, beta):
    if (depth == 0 or ((node.left == None and node.right == None))):
            node.dynamicValue = node.heuristicValue
            return ntraversedNodes, node.heuristicValue
        
    if isMaximisingPlayer:
        maxEval = -10000
        if (node.left != None):
            ntraversedNodes, maxEval, alpha = alphaBetaMax(ntraversedNodes, node.left, depth, False, alpha, beta, maxEval)

        if (not(beta <= alpha)):
            if (node.right != None):
                ntraversedNodes, maxEval, beta = alphaBetaMax(ntraversedNodes, node.right, depth, False, alpha, beta, maxEval)

        node.dynamicValue = maxEval
        return ntraversedNodes, maxEval
    
    else:
        minEval = 10000
        if (node.left != None):
            ntraversedNodes, minEval, beta = alphaBetaMin(ntraversedNodes, node.left, depth, True, alpha, beta, minEval)

        if (not(beta <= alpha)):
            if (node.right != None):
                ntraversedNodes, minEval, beta = alphaBetaMin(ntraversedNodes, node.right, depth, True, alpha, beta, minEval)

        
        node.dynamicValue = minEval
        return ntraversedNodes, minEval
    
def alphaBetaMax(ntraversedNodes, node, depth, isMaximisingPlayer, alpha, beta, maxEval):
    ntraversedNodes, eval = alphaBeta(ntraversedNodes, node, depth - 1, False, alpha, beta)
    maxEval = max(maxEval, eval)
    alpha = max(alpha, eval)
    ntraversedNodes+=1
    return ntraversedNodes, maxEval, alpha

def alphaBetaMin(ntraversedNodes, node, depth, isMaximisingPlayer, alpha, beta, minEval):
    ntraversedNodes, eval = alphaBeta(ntraversedNodes, node, depth - 1, True, alpha, beta)
    minEval = min(minEval, eval)
    beta = min(beta, eval)
    ntraversedNodes+=1
    return ntraversedNodes, minEval, beta



# Pievienotā GameEngine klase, lai varam apvienot loģiku ar GUI

# komentari šim un gui ir ģenerēti :)

class GameEngine:
    def __init__(self, start_number, algorithm=1, player_vs_ai=True):
        # Inicializē spēles dzinēju ar sākuma skaitli, algoritma izvēli un spēles režīmu (cilvēks pret datoru)
        # algorithm: 1 = minimax, 2 = alphaBeta
        self.tree = gameTree(start_number)  # Izveido spēles koku, izmantojot start_number kā sākuma vērtību
        self.current = self.tree.root       # Saglabā sākuma stāvokli no koka saknes
        self.player_vs_ai = player_vs_ai    # Saglabā informāciju par to, vai spēle ir cilvēks pret datoru
        self.algorithm = algorithm          # Saglabā izvēlēto algoritmu (1 vai 2)    
        self.traversedNodes = 0
        print("init",self.player_vs_ai)

    def get_state(self):
        # Atgriež pašreizējo spēles stāvokli kā vārdnīcu, ko var izmantot GUI interfeisā
        print("getting state", self.player_vs_ai)
        if self.player_vs_ai:
            return {
                "skaitlis": self.current.number,         # Pašreizējais skaitlis
                "cilvēks": self.current.player1Pts,      # Spēlētāja punkti
                "dators": self.current.player2Pts,       # Datora punkti
                #"turn": self.current.currentPlayer       # Kurš veic nākamo gājienu 
            }
        else:
            return {
                "skaitlis": self.current.number,         # Pašreizējais skaitlis
                "dators1": self.current.player1Pts,      # Spēlētāja punkti
                "dators2": self.current.player2Pts,      # Datora punkti
                #"turn": self.current.currentPlayer       # Kurš veic nākamo gājienu 
            }

    def is_game_over(self):
        # Pārbauda, vai spēle ir beigusies:
        # Spēle beidzas, ja pašreizējais skaitlis ir mazāks vai vienāds ar 10 vai ja skaitli vairs nevar dalīt ar 2 vai 3.
        return self.current.number <= 10 or (self.current.number % 2 != 0 and self.current.number % 3 != 0)

    def make_player_move(self, divisor):
        
        # Veic spēlētāja gājienu, ja tas ir atļauts:
        # Pārbauda, vai nākamais gājiens ir spēlētājam un vai pašreizējais skaitlis dalās ar norādīto divisor (2 vai 3).
        if self.current.currentPlayer == "player" and self.current.number % divisor == 0 :
            self.current.number //= divisor  # Dalās ar divisor, atjaunojot skaitli
            # Pāriet uz atbilstošo apakšmezglu (koka mezglu) atkarībā no izvēlētā dalītāja
            if divisor == 3 and self.current.left is not None:
                self.current = self.current.left
            elif divisor == 2 and self.current.right is not None:
                self.current = self.current.right
            return True  # Gājiens veiksmīgi izpildīts
      
        return False  # Ja nosacījumi netiek izpildīti, gājiens nav veiksmīgs

    def make_ai_move(self):
        # Veic datora (AI) gājienu, ja nākamais gājiens ir "computer" tad minimizē, ja "player" tad maximizē
        ntraversedNodes = 0

        isMaximising = False
        if self.current.currentPlayer == "computer":
            isMaximising = False
        else:
            isMaximising = True


        goTroughAlgorythm = True        
        try:
            if (self.current.left.dynamicValue == self.current.dynamicValue and not (self.current.dynamicValue == -6000)):
                if not (self.current.left.dynamicValue == -6000):
                    goTroughAlgorythm = False
                else:
                    goTroughAlgorythm = True
        except:
            pass

        try:    
            if self.current.right.dynamicValue == self.current.dynamicValue and not (self.current.dynamicValue == -6000): 
                if not (self.current.right.dynamicValue == -6000):
                    goTroughAlgorythm = False
                else:
                    goTroughAlgorythm = True
        except:
            pass


        SEARCH_DEPTH = 10
        if goTroughAlgorythm:

            if self.algorithm == 1:
                ntraversedNodes, eval = minimax(ntraversedNodes, self.current, SEARCH_DEPTH, isMaximising) 

            else:
                ntraversedNodes, eval = alphaBeta(ntraversedNodes, self.current, SEARCH_DEPTH, isMaximising, -10000, 10000)

        print(ntraversedNodes)
        

        # Pārbauda, kurš apakšmezgls atbilst aprēķinātajam vērtējumam:

        # Ja Kreisais (dalīšana ar 3) apakšmezgls ir derīgs un tā dinamiskā vērtība sakrīt ar pašreizējo, tad veic gājienu
        if self.current.left is not None and self.current.left.dynamicValue == self.current.dynamicValue:
            self.current.number //= 3
            self.current = self.current.left

        # Pretējā gadījumā, ja labo (dalīšana ar 3) apakšmezgls atbilst, tad veic gājienu        
        elif self.current.right is not None and self.current.right.dynamicValue == self.current.dynamicValue:
            self.current.number //= 2
            self.current = self.current.right
        
        
        
   
if __name__ == '__main__':
    main()
