import random
def rollDie():
    return random.choice([1,2,3,4,5,6])
    
class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0
    
    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break
                
    """def passResults(self):
        return (self.passWins, self.passLosses)
    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)"""
    
def deneme(sayi):
    c = CrapsGame()
    for i in range(sayi):
        c.playHand()
    print(c.passWins / sayi)
        
deneme(50)       
print()        
        
c = CrapsGame()
c.playHand()
print("kazandin -> ",c.passWins)
print("kaybettin -> ",c.passLosses)

print("\nkumarane kazandi ->",c.dpWins)
print("kumarane kaybetti ->",c.dpLosses)
print("12 geldi ->",c.dpPushes)

"""print(c.passResults())
print(c.dpResults())"""

#--------------------------

def check_pascal(num_trials):
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if(d1 == 6 and d2 == 6):
                num_wins += 1
                break
    print(num_wins / num_trials)
    
check_pascal(100)