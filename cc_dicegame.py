import random

high_score = 0

def dice_game():
    
        global high_score
        
        while True:
            print("Current High Score",high_score)
            print("1) Roll Dice")
            print("2) Leave Game")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                dice_1 = random.randint(1,6)
                dice_2 = random.randint(1,6)
                print("You roll a...",dice_1)
                print("You roll a ...",dice_2)
                total = dice_1 + dice_2
                print("You have rolled a total of: ",total,"\n")
            elif total > high_score:
                print("New High Score!\n")
                high_score = total
            elif choice == "2":
                print("You have left the game")
                break
            else:
                print("Unknown Choice. Retry")
                continue
dice_game()