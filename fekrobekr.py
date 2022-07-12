import random

colors = ['red ', 'blue', 'green', 'yellow', 'firoozeh', 'purple', 'orange', 'pink', 'white', 'black']

class Player():
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn
        self.known_colors = ['unknown']*4
    
    def add_turn(self):
        self.turn += 1

    def get_turn(self):
        return self.turn
    
    def get_name(self):
        return self.name

    def add_color(self, color, idx):
        self.known_colors[idx] = color

    def get_known_colors(self):
        return self.known_colors

class Game():
    def __init__(self):
        self.N = 4
        self.color_list = []
        for _ in range(self.N):
            rand_idx = random.randint(0, len(colors)-1)
            self.color_list.append(colors[rand_idx])
    
    def check_color_list(self, guessed_colors, player):
        for i in range(self.N):
            if guessed_colors[i] == self.color_list[i]:
                player.add_color(guessed_colors[i], i)
        player.add_turn()
    
    def win_check(self, player):
        colors = player.get_known_colors()
        hasWon = False
        for i in range(self.N):
            if self.color_list[i] == colors[i]:
                hasWon = True
            if not hasWon:
                return False
        return True

    def get_color_list(self):
        return self.color_list

''' STARTING THE GAME'''

TURNS = 10
NUM_PLAYER = 3
PLAYER_LIST = []
for i in range(NUM_PLAYER):
    print("Please write your name...(should be unique)")
    player_name = str(input())
    player = Player(player_name, 1)
    PLAYER_LIST.append(player)

game = Game()
'''
cheat = game.get_color_list()
print(*cheat)
'''

I = 0
for I in range(TURNS):
    print("TURN " + str(I+1))
    hasWon = False
    for i in range(NUM_PLAYER):
        current_player = PLAYER_LIST[i]
        print("player " + current_player.name + ": Please enter the colors in order...")
        print("known_colors: ")
        print(*current_player.known_colors)
        guessed_colors = list(map(str, input().strip().split()))[:4]
        game.check_color_list(guessed_colors, current_player)
        hasWon = game.win_check(current_player)
        if hasWon:
            print("Player " + current_player.get_name() + " has won!")
            break

    if hasWon:
        break

if I+1 == TURNS:
    print("No winners :(")