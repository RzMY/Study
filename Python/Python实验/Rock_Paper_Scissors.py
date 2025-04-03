class computer:
    def __init__(self):
        self.score = 0
        self.choice = 0

    def get_choice(self):
        import random
        self.choice = random.randint(1, 3)

    def show_choice(self):
        if self.choice == 1:
            print("Computer: 石头")
        elif self.choice == 2:
            print("Computer: 剪刀")
        else:
            print("Computer: 布")
    
class player:
    def __init__(self):
        self.score = 0
        self.choice = 0

    def get_choice(self):
        self.choice = int(input("请输入你的选择：1.石头 2.剪刀 3.布\n"))

    def show_choice(self):
        if self.choice == 1:
            print("Player: 石头")
        elif self.choice == 2:
            print("Player: 剪刀")
        else:
            print("Player: 布")
            
def judge(player, computer):
    if player.choice == computer.choice:
        print("平局")
    elif player.choice == 1 and computer.choice == 2:
        print("Player Win")
        player.score += 1
    elif player.choice == 2 and computer.choice == 3:
        print("Player Win")
        player.score += 1
    elif player.choice == 3 and computer.choice == 1:
        print("Player Win")
        player.score += 1
    else:
        print("Computer Win")
        computer.score += 1
        
def show_score(player, computer):
    print("Player: %d, Computer: %d" % (player.score, computer.score))
    
def main():
    p = player()
    c = computer()
    while True:
        p.get_choice()
        c.get_choice()
        p.show_choice()
        c.show_choice()
        judge(p, c)
        show_score(p, c)
        if p.score == 2 or c.score == 2:
            print("Game Over, %s Win" % ("Player" if p.score == 2 else "Computer"))
            break
        
if __name__ == "__main__":
    main()