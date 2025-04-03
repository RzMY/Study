import random

class computer:
    def __init__(self):
        self.hp = 100
        self.attack = 0
        self.name = "电脑"

    def get_attack(self):
        import random
        self.attack = random.randint(30, 60)

    def show_attack(self):
        print("%s对玩家造成%d点伤害" % (self.name, self.attack))
        
class player:
    def __init__(self):
        self.hp = 100
        self.attack = 0
        self.name = "玩家"

    def get_attack(self):
        print("请选择你的攻击方式：")
        print("1.普通攻击 2.大招")
        self.attack = int(input())
        if self.attack == 1:
            self.attack = random.randint(30, 50)
        else:
            self.attack = random.randint(40, 60)

    def show_attack(self):
        print("%s对电脑造成%d点伤害" % (self.name, self.attack))
        
def judge(player, computer):
    player.hp -= computer.attack
    computer.hp -= player.attack
    print("玩家 HP: %d, 电脑 HP: %d" % (player.hp, computer.hp))
    print("----------------------------------------------")
    if player.hp <= 0 and computer.hp <= 0:
        if player.hp >= computer.hp:
            print("玩家赢了")
            return 'player'
        else:
            print("电脑赢了")
            return 'computer'
    elif player.hp <= 0:
        print("电脑赢了")
        return 'computer'
    elif computer.hp <= 0:
        print("玩家赢了")
        return 'player'
    else:
        return None
    
def printStatus(player, computer, round):
    print("--------------------回合 %d--------------------" % round)
    print("玩家 HP: %d, 电脑 HP: %d" % (player.hp, computer.hp))
    
def main():
    player_wins = 0
    computer_wins = 0
    round = 1
    while player_wins < 2 and computer_wins < 2:
        p = player()
        c = computer()
        printStatus(p, c, round)
        while True:
            p.get_attack()
            c.get_attack()
            p.show_attack()
            c.show_attack()
            winner = judge(p, c)
            if winner is not None:
                if winner == 'player':
                    player_wins += 1
                else:
                    computer_wins += 1
                break
        round += 1
    print("-------------------比赛结束-------------------")
    if player_wins > computer_wins:
        print("最终结果：玩家赢得了比赛！")
    else:
        print("最终结果：电脑赢得了比赛！")
        
if __name__ == "__main__":
    main()