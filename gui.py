import tkinter as tk
import random
from main import GameEngine  # Importē spēles dzinēja klasi no main.py

# spēle jāpalaiž no šī faila 

class GameGUI:
    def __init__(self, root):
        # Inicializē GUI ar norādīto Tkinter logu (root)
        self.root = root
        self.root.title("Number Division Game")  # Iestata loga nosaukumu
        self.root.geometry("500x590")  # Iestata loga izmērus
        
        # Ģenerē sākuma skaitļus (5 skaitļi no 10000 līdz 20000, kuri dalās ar 2 un 3)
        self.generated_numbers = self.generate_starting_numbers()
        
        # Izveido un sakārto GUI elementus
        self.setup_ui()

        self.engine = None  # Spēles dzinējs (GameEngine instance), kas tiks inicializēts, kad spēle sāksies
    
    def generate_starting_numbers(self):
        # Atgriež 5 sākuma skaitļus, kas atbilst nosacījumiem (dalās ar 2 un 3)
        start = []
        for i in range(5):
            start.append(6*random.randint(1667, 3333))
        return start
    
    def setup_ui(self):
        # Galvenā nosaukuma etiķete
        self.frameNums = tk.Frame(self.root)
        self.frameNums.pack()

        tk.Label(self.frameNums, text="Number Division Game", font=("Arial", 16)).pack(pady=10)
        
        # Sākuma skaitļa izvēles sadaļa
        tk.Label(self.frameNums, text="Choose a starting number:").pack()
        self.start_number_var = tk.IntVar(value=self.generated_numbers[0])  # Saglabā izvēlēto sākuma skaitli
        # Izveido radio pogas katram no ģenerētajiem skaitļiem
        for num in self.generated_numbers:
            tk.Radiobutton(self.frameNums, text=str(num), variable=self.start_number_var, value=num).pack()
        
        # Algoritma izvēles sadaļa
        tk.Label(self.frameNums, text="Choose Algorithm:").pack(pady=(10, 0))
        self.algorithm_var = tk.IntVar(value=1)  # Noklusēti: 1 = Minimax, 2 = Alpha-Beta
        self.algo_frame = tk.Frame(self.root)
        self.algo_frame.pack()
        # Izveido radio pogas algoritmu izvēlei
        tk.Radiobutton(self.algo_frame, text="Minimax", variable=self.algorithm_var, value=1).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.algo_frame, text="Alpha-Beta", variable=self.algorithm_var, value=2).pack(side=tk.LEFT, padx=5)


        self.player1_frame = tk.Frame(self.root)
        self.player1_frame.pack()
        tk.Label(self.player1_frame, text="Izvelaties kurš spēlē kā spēlētājs:").pack(pady=(10, 0))
        self.player_vs_ai = tk.BooleanVar(value=True)  # Noklusēti: 1 = Minimax, 2 = Alpha-Beta
        
        
        tk.Radiobutton(self.player1_frame, text="Speletajs", variable=self.player_vs_ai, value=True).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.player1_frame, text="Dators", variable=self.player_vs_ai, value=False).pack(side=tk.LEFT, padx=5)
        
        #self.startGameFrame = tk.Frame(self.root)
        #self.startGameFrame.pack()
        # Poga, lai uzsāktu spēli
        self.startButton = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.startButton.pack(pady=5)
        
        # Informācijas rāmis, kurā tiks parādīts spēles statuss
        self.info = tk.Frame(self.root)
        self.info.pack(pady=10)
        
        # Etiķetes un vērtības, kas parāda pašreizējo skaitli, spēlētāja un datora punktus un kurš gājas nākamais
        tk.Label(self.info, text="Current Number:").grid(row=0, column=0)
        self.current_number = tk.Label(self.info, text="--")
        self.current_number.grid(row=0, column=1)
        
        tk.Label(self.info, text="Player Score:").grid(row=1, column=0)
        self.human_score = tk.Label(self.info, text="0")
        self.human_score.grid(row=1, column=1)
        
        tk.Label(self.info, text="Computer Score:").grid(row=2, column=0)
        self.computer_score = tk.Label(self.info, text="0")
        self.computer_score.grid(row=2, column=1)
        
        tk.Label(self.info, text="Current Player:").grid(row=3, column=0)
        self.current_player = tk.Label(self.info, text="--")
        self.current_player.grid(row=3, column=1)
        
        # Rāmis, kurā tiek izvietotas gājiena pogas
        self.button = tk.Frame(self.root)
        self.button.pack()
        
        # Izveido pogas dalīšanai ar 2 un 3; sākotnēji tās ir atspējotas
        self.buttonDivide2 = tk.Button(self.button, text="Divide by 2", state=tk.DISABLED, command=lambda: self.make_move(2))
        self.buttonDivide3 = tk.Button(self.button, text="Divide by 3", state=tk.DISABLED, command=lambda: self.make_move(3))
               
        # Novieto pogas režģī
        self.buttonDivide2.grid(row=0, column=0, padx=5, pady=5)
        self.buttonDivide3.grid(row=0, column=1, padx=5, pady=5)
        
        # Restart poga, lai sāktu spēli no jauna
        #self.restartButtonFrame = tk.Frame(self.root)
        self.restart_button = tk.Button(self.root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack(pady=10)
    
    def start_game(self):
        # Saglabā izvēlēto sākuma skaitli un algoritma vērtību
        start_number = self.start_number_var.get()
        #start_number = 19440 #test
        selected_algorithm = self.algorithm_var.get()  # Iegūst vērtību: 1 = Minimax, 2 = Alpha-Beta
        player_vs_ai = self.player_vs_ai.get()
        # Inicializē spēles dzinēju (GameEngine) ar izvēlēto sākuma skaitli un algoritmu
        self.engine = GameEngine(start_number, algorithm=selected_algorithm, player_vs_ai=True)
        self.update_ui()  # Atjaunina GUI, lai parādītu spēles sākuma stāvokli
        print(player_vs_ai)
        if player_vs_ai:
            
            self.enable_move_buttons()  # Ieslēdz gājiena pogas
        else:
            while not self.engine.is_game_over():
                self.computer_turn()
        
        try:
            self.labelWinner.destroy()
        except:
            pass

    def enable_move_buttons(self):
        # Ieslēdz pogas, lai spēlētājs varētu veikt gājienus
        self.buttonDivide2.config(state=tk.NORMAL)
        self.buttonDivide3.config(state=tk.NORMAL)
    
    def disable_move_buttons(self):
        # Atspējo gājiena pogas
        self.buttonDivide2.config(state=tk.DISABLED)
        self.buttonDivide3.config(state=tk.DISABLED)
    
    def make_move(self, divisor):
        # Veic spēlētāja gājienu ar norādīto dalītāju (2 vai 3)
        if self.engine:
            if self.engine.make_player_move(divisor):
                self.update_ui()  # Atjaunina GUI pēc spēlētāja gājiena
                if self.engine.is_game_over():
                    self.end_game()  # Pārbauda, vai spēle ir beigusies
                else:
                    # Dod datoram nedaudz laika (500 ms), pirms izsauc datorgājienu
                    self.root.after(500, self.computer_turn)
    
    def computer_turn(self):
        # Veic datorgājienu
        
        if self.engine:
            self.engine.make_ai_move()
            
            self.update_ui()  # Atjaunina GUI pēc datorgājiena
            if self.engine.is_game_over():
                self.end_game()  # Ja spēle ir beigusies, izsauc beigu funkciju
        
    
    def update_ui(self): 
        # Iegūst spēles stāvokli no GameEngine un atjaunina GUI elementus
        state = self.engine.get_state()
        self.current_number.config(text=str(state["number"]))
        self.human_score.config(text=str(state["player_score"]))
        self.computer_score.config(text=str(state["computer_score"]))
        self.current_player.config(text=state["turn"])
    
    def end_game(self):
        # Kad spēle ir beigusies, atspējo gājiena pogas un parāda rezultātu
        
        self.disable_move_buttons()
        state = self.engine.get_state()
        winner = "Player" if state["player_score"] > state["computer_score"] else "Computer"
        self.labelWinner = tk.Label(self.root, text=f"Game Over! Winner: {winner}", font=("Arial", 14))
        self.labelWinner.pack()
    
    def restart_game(self):
        # Atiestata GUI elementus uz sākotnējo stāvokli un atiestata spēles dzinēju
        self.current_number.config(text="--")
        self.human_score.config(text="0")
        self.computer_score.config(text="0")
        self.current_player.config(text="--")
        self.disable_move_buttons()
        self.generated_numbers = self.generate_starting_numbers()
        
        self.destroyFrames()

        ##!
        self.setup_ui()

        self.engine = None  # Notīra esošo spēles dzinēju

    def destroyFrames(self):
        self.frameNums.destroy()
        self.algo_frame.destroy()
        self.player1_frame.destroy()
        #self.startGameFrame.destroy()
        self.info.destroy()
        self.button.destroy()
        self.startButton.destroy()
        self.restart_button.destroy()
        self.labelWinner.destroy()
        #self.engine.




if __name__ == "__main__":
    root = tk.Tk()           # Izveido galveno Tkinter logu
    game_gui = GameGUI(root) # Inicializē GameGUI klasi ar logu
    root.mainloop()          # Sāk Tkinter galveno notikumu cilpu
