import random

def game_win(user, computer):
    if user == computer:
        return None
    

 # snake vs water
    if user == "s" and computer == "w":
        return True

    if user == "w" and computer == "s":
        return False


 # water vs gun
    if user == "w" and computer == "g":
        return True

    if user == "g" and computer == "w":
        return False


 # gun vs snake
    if user == "g" and computer == "s":
        return True

    if user == "s" and computer == "g":
        return False


rand_no = random.randint(1,3)


#computer turn
print("Computer's Turn : Snake(s), Water(w), Gun(g)")
if rand_no == 1:
    computer = "s"

elif rand_no == 2:
    computer = "w"

else:
    computer = "g"


#user turn
user = input("Your Turn : Snake(s), Water(w), Gun(g): ").lower()   #.lower() will convert the capital string(alphhabet) into smaller one

result = game_win(user, computer)

print(f"\n You choose : {user}")
print(f"\n Computer choose : {computer}")

if result is None:
    print("It's a draw")

elif(result):
    print("You win!")

else:
    print("You lose!")