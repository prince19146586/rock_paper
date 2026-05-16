import random 
print("welcome to rock , paper , scissors game!! \nto end the game and see you score type : end")
score = 0
bot_score = 0
no_of_game_plays = 0
draw = 0
list1 = ["r" , "p" , "s" , "rock" , "paper" , "scissors" , "end" , "END"]

while True:
    rand = random.randint(1,3)
    
        
    ask = input("select rock , paper , scissors (r,p,s) : ").lower()
    no_of_game_plays += 1

      
    if ask not in list1:
      
        print("invalid input \ntry again!!...")
        no_of_game_plays -= 1
      
        continue
      
        

    


    if ask.lower() == "end":
        print(f"thank for playing , you have played {no_of_game_plays - 1} numbers of rounds")

        print(f"your score is : {score}/{no_of_game_plays - 1} \ncomputer score is : {bot_score}/{no_of_game_plays - 1} \nNO of draw match : {draw}") 

        break
    
    elif rand == 1:
        print("computer chose : rock ")

        if ask == "s":

            print("you lose!")

            bot_score += 1

        elif ask == "p":
            print("you win!")

            score += 1

        elif ask == "r":
            print("draw!")

            draw += 1

        

    elif rand == 2:
        print("computer close : paper")

        if ask == "r":
            print("you lose!")

            bot_score += 1

        elif ask == "s":
            print("you win!")

            score += 1

        elif ask == "p":

            print("draw!")

            draw += 1 

            



    elif rand == 3:
        print("computer chose : scissors")

        if ask == "p":
            print("you lose!")

            bot_score += 1

        elif ask == "r":

            print("you win!")

            score += 1

        elif ask == "s":

            print("draw!")

            draw += 1

        
