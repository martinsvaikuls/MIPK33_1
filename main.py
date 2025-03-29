import random


class gameNode:
    def __init__(self, number, p1, p2, nextTurn, left, right, staticValue, dynamicValue):      # p1 = player, p2 = computer
        self.number = number                                        # p1 | num | p2
        self.p1 = p1                                                #  0 | 999 | 0
        self.p2 = p2                                                
        self.nextTurn = nextTurn    
        self.left = left                                          
        self.right = right
        self.staticValue = staticValue
        self.dynamicValue = dynamicValue
        



class gameTree:
    def __init__(self, number):
        self.root = self.build(gameNode(number, 0, 0, "player", None, None, 0, -3621), 1)
        self.print_tree(self.root)
    

    def build(self, node, num):
        gameList = ["player","computer"]
                # ja bus svarigi
        nt = gameList[num]
        if (node.number >= 10):
            if (num == 0):
                num = 1
                if(node.number % 2 == 0):
                    staticValue = node.p1 - node.p2 + 0
                    node.right = gameNode(node.number//2, node.p1+2, node.p2, nt, None, None, staticValue, -3621)
                    self.build(node.right, num)

                if(node.number % 3 == 0):
                    staticValue = node.p1 - node.p2 + 2
                    node.left = gameNode(node.number//3, node.p1, node.p2+3, nt, None, None, staticValue, -3621)
                    self.build(node.left, num)
            else:
                num = 0
                if(node.number % 2 == 0):
                    staticValue = node.p1 - node.p2 + 0
                    node.right = gameNode(node.number//2, node.p1, node.p2+2, nt, None, None, staticValue, -3621)
                    self.build(node.right, num)

                if(node.number % 3 == 0):
                    staticValue = node.p1 - node.p2 + 2
                    node.left = gameNode(node.number//3, node.p1+3, node.p2, nt, None, None, staticValue, -3621)
                    self.build(node.left, num)
            
            return node
    

    # --- CHAT GPT
    def print_tree(self, node, level=0): 
        #"""
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.number, node.nextTurn, node.p1, node.p2, node.staticValue)
            self.print_tree(node.left, level + 1)
        #"""
     # --- CHAT GPT


# Nemts no interneta video
def minimax(ntraversedNodes, node, depth, isMaximisingPlayer):
    if (depth == 0 or ((node.left == None and node.right == None))):
        node.dynamicValue = node.staticValue
        return ntraversedNodes, node.staticValue
    
    #print(ntraversedNodes)
    if isMaximisingPlayer:
        maxEval = -10000
        if (node.left != None):
            ntraversedNodes, eval = minimax(ntraversedNodes, node.left, depth - 1, False)
            maxEval = max(maxEval, eval)
            ntraversedNodes+=1
        #print(ntraversedNodes)
        if (node.right != None):
            ntraversedNodes,eval = minimax(ntraversedNodes, node.right, depth - 1, False)
            maxEval = max(maxEval, eval)
            ntraversedNodes+=1

        node.dynamicValue = maxEval
        #print(ntraversedNodes)
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
        #print(ntraversedNodes)
        return ntraversedNodes, minEval
    

def alphaBeta(ntraversedNodes, node, depth, isMaximisingPlayer, alpha, beta):
    if (depth == 0 or ((node.left == None and node.right == None))):
            node.dynamicValue = node.staticValue
            return ntraversedNodes, node.staticValue
        
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

    def get_state(self):
        # Atgriež pašreizējo spēles stāvokli kā vārdnīcu, ko var izmantot GUI interfeisā
        if self.player_vs_ai:
            return {
                "skaitlis": self.current.number,           # Pašreizējais skaitlis
                "spēlētājs": self.current.p1,         # Spēlētāja punkti
                "dators": self.current.p2,       # Datora punkti
                "turn": self.current.nextTurn            # Kurš veic nākamo gājienu ("player" vai "computer")
            }
        else:
            return {
                "skaitlis": self.current.number,           # Pašreizējais skaitlis
                "dators1": self.current.p1,         # Spēlētāja punkti
                "dators2": self.current.p2,       # Datora punkti
                "turn": self.current.nextTurn            # Kurš veic nākamo gājienu ("player" vai "computer")
            }

    def is_game_over(self):
        # Pārbauda, vai spēle ir beigusies:
        # Spēle beidzas, ja pašreizējais skaitlis ir mazāks vai vienāds ar 10 vai ja skaitli vairs nevar dalīt ar 2 vai 3.
        return self.current.number <= 10 or (self.current.number % 2 != 0 and self.current.number % 3 != 0)

    def make_player_move(self, divisor):
        
        # Veic spēlētāja gājienu, ja tas ir atļauts:
        # Pārbauda, vai nākamais gājiens ir spēlētājam un vai pašreizējais skaitlis dalās ar norādīto divisor (2 vai 3).
        if self.current.nextTurn == "player" and self.current.number % divisor == 0 :
            self.current.number //= divisor  # Dalās ar divisor, atjaunojot skaitli
            # Pāriet uz atbilstošo apakšmezglu (koka mezglu) atkarībā no izvēlētā dalītāja
            if divisor == 3 and self.current.left is not None:
                self.current = self.current.left
            elif divisor == 2 and self.current.right is not None:
                self.current = self.current.right
            return True  # Gājiens veiksmīgi izpildīts
      
        return False  # Ja nosacījumi netiek izpildīti, gājiens nav veiksmīgs

    def make_ai_move(self):
        # Veic datora (AI) gājienu, ja nākamais gājiens ir datoram
        #if self.current.nextTurn == "computer":
            # Izvēlas algoritmu atkarībā no izvēles (1 = minimax, 2 = alphaBeta)
        ntraversedNodes = 0
        isMaximising = False
        if self.current.nextTurn == "computer":
            isMaximising = False
        else:
            isMaximising = True

        goTroughAlgorythm = True

        
        try:
            if (self.current.left.dynamicValue == self.current.dynamicValue and not (self.current.dynamicValue == -3621)):
                if not (self.current.left.dynamicValue == -3621):
                    goTroughAlgorythm = False
                else:
                    goTroughAlgorythm = True
                
        except:
            pass
        try:    
            if self.current.right.dynamicValue == self.current.dynamicValue and not (self.current.dynamicValue == -3621): 
                if not (self.current.right.dynamicValue == -3621):
                    goTroughAlgorythm = False
                else:
                    goTroughAlgorythm = True
        except:
            pass

        if goTroughAlgorythm:
            #print("algo")
            if self.algorithm == 1:
                ntraversedNodes, eval = minimax(ntraversedNodes, self.current, 40, isMaximising)  # Izsauc minimax algoritmu ar dziļumu 4
                #print('minimax')
            else:
                ntraversedNodes, eval = alphaBeta(ntraversedNodes, self.current, 40, isMaximising, -10000, 10000)  # Izsauc alphaBeta algoritmu ar dziļumu 4 un sākotnējiem alpha, beta vērtībām
                #print('alfabeta')
                
        print(ntraversedNodes)
         # Pārbauda, kurš apakšmezgls atbilst aprēķinātajam vērtējumam:
        # Ja kreisais (dalīšana ar 2) apakšmezgls ir derīgs un tā dinamiskā vērtība sakrīt ar pašreizējo, tad veic gājienu
        """
        print(self.current.nextTurn)       
        print(self.current.dynamicValue)

        
        try:
            print("left ",self.current.left.dynamicValue, end="")
        except:
            pass

        try:
            print(" right",self.current.right.dynamicValue)
        except:
            pass
        """
        
        # Pretējā gadījumā, ja labo (dalīšana ar 3) apakšmezgls atbilst, tad veic gājienu
        if self.current.left is not None and self.current.left.dynamicValue == self.current.dynamicValue:
            #print("left")
            self.current.number //= 3
            self.current = self.current.left
        elif self.current.right is not None and self.current.right.dynamicValue == self.current.dynamicValue:
            #print("right")
            self.current.number //= 2
            self.current = self.current.right
        
        
        

        
       


        
if __name__ == '__main__':
    main()
