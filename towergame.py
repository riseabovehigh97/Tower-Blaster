# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:07:22 2020

@author: Ali
"""

#Tower Blaster 

#Shuffler
def shuffle(b):
    import random
    random.shuffle(b)
    
#Check b
def check_b(main_pile,discard):
    if len(main_pile) == 0:
        shuffle(discard)
        main_pile.extend(discard)
        discard = []
        x = main_pile.pop(0)
        discard.append(x)
        
#Sorting
def check_tower_blaster(tower):
    if tower == sorted(tower):
        return True
    else:
        return False

#find top brick
def get_top_brick(brick_pile):
    top_element = brick_pile.pop(0)
    return int(top_element)

#initial
def deal_initial_b(main_pile):
    user_pile =[]
    computer_pile =[]
    shuffle(main_pile)
    for i in range(20):
        if i % 2 == 0:
            computer_pile.insert(0,get_top_brick(main_pile))
            shuffle(main_pile)
        else:
            user_pile.insert(0,get_top_brick(main_pile))
            shuffle(main_pile)
    return (user_pile, computer_pile)

#Adding            
def add_brick_to_discard(brick,	discard):
    discard.insert(0,brick)

#Replacing 
def find_and_replace(new_brick,	brick_to_be_replaced, tower, discard):
    if brick_to_be_replaced in tower:
        pos = tower.index(brick_to_be_replaced)
        add_brick_to_discard(tower[pos],discard)
        tower[pos] = new_brick
        return True
    else:
        return False

turn = 0 

#Comp player
def computer_play(tower, main_pile, discard):
    global turn
    if turn % 5 == 0:
        brick = get_top_brick(main_pile)
        if turn % 4 == 0:
            add_brick_to_discard(brick,discard)
            turn +=1
        else:
            turn +=1
            if brick in range(1,31):
                if brick in range(1,16):
                    for i in range(0,10):
                        if tower[i] > brick:
                            find_and_replace(brick,tower[i],tower,discard)
                            break
                else:
                    for i in range(9,-1,-1):
                        if tower[i] < brick:
                            find_and_replace(brick,tower[i],tower,discard)
                            break
            else:
                if brick in range(31,46):
                    for i in range(0,10):
                        if tower[i] > brick:
                            find_and_replace(brick,tower[i],tower,discard)
                            break
                else:
                    for i in range(9,-1,-1):
                        if tower[i] < brick:
                            find_and_replace(brick,tower[i],tower,discard)
                            break
                    
    else:
       turn +=1
       brick = get_top_brick(discard)
       if brick in range(1,31):
           for i in range(0,10):
               if tower[i] > brick:
                    find_and_replace(brick,tower[i],tower,discard)
                    break
       else:
            for i in range(9,-1,-1):
                if tower[i] < brick:
                    find_and_replace(brick,tower[i],tower,discard)
                    break
    return tower
#check if user want to replace or not 
def replace_b_in_tower(number,user_pile,discard):
    brick_to_replace = input("Enter the brick to be replace in tower: ")
    check_list = [str(i) for i in range(1,61)]
    while brick_to_replace not in check_list:
        brick_to_replace = input("!!Wrong Value Entered. Enter Valid Input: ")
    brick_to_replace = int(brick_to_replace)
    while not (find_and_replace(number,brick_to_replace, user_pile, discard)):
         print("Brick Not Found")
         brick_to_replace = int(input("Enter the brick to be replace: "))
         continue
    return user_pile


def check_user_choice(choice, tower, main_pile, discard):
    while choice != "Y" and choice !="y" and choice !="N" and choice !="n":
        choice = input("!! Invalid Option !! Enter a valid choice [Y/N] ")  
        
    if choice == "N" or choice == "n":
           num = get_top_brick(discard)
           tower = replace_b_in_tower(num,tower,discard)
           
    elif choice == "Y" or choice == "y":
            num = get_top_brick(main_pile)
            c = input("Do you wish to use " + str(num) + ". [Enter Y or N] - ")
            while c != "Y" and c !="y" and c != "N" and c != "n":
                c = input("!! Invalid Option !! Enter a valid choice [Y/N] ")
                
            if c == "N" or c == "n":
                add_brick_to_discard(num,discard)
            elif c == "Y" or c == "y":
                 tower = replace_b_in_tower(num,tower,discard)                         
    return tower               
                        
def main():

    print("******++++++++++Tower Blaster++++++++++****** \n")
    computer_tower = []
    user_tower = []
    main_pile = [i for i in range(1,61)]
    discard = []
    
    user_tower, computer_tower = deal_initial_b(main_pile)

    discard.append(get_top_brick(main_pile))

    print("********* Player 2 Turns *********")
    print("Player 1: Tower \t Player 2: Tower")
    for i in range(10):
        print("\t\t\t" + str(computer_tower[i]) + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(user_tower[i]))

    while True:
        check_b(main_pile,discard)
        computer_tower = computer_play(computer_tower, main_pile,discard)
        if check_tower_blaster(computer_tower) == True:
            print("....SORRY, YOU LOST.BETTER LUCK NEXT TIME.... ")
            break
        else:
            discard_pile_num = discard[0]
            print("Available Number is " + str(discard_pile_num))
            print("Do you want this number or goto the main pile.")
            user_choice = input("Enter Y for the main pile and N to continue: ")
            user_tower = check_user_choice(user_choice, user_tower,main_pile,discard)

            if check_tower_blaster(user_tower) == True:
                print("Player 2: Tower")
                for i in range(10):
                    print("\t",user_tower[i])
                print("#*#*CONGRATULATIONS*#*#:) !!YOU WON!!")
                break  
            print("Player 2: Tower")
            for i in range(10):
                print("\t",user_tower[i])
if __name__ == '__main__':
    main()