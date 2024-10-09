def grid(a,logic):
    for i in range(a):
        for j in range(a):  
            print(f"{(i*a)+j+11}{logic[0][j+(i*a)]}",end="")
        print()
        for k in range(a):
            print(f"{logic[1][k+(i*a)]}",end = "") 
        print()
         
def joininggrid(a,logic,x):
    
    while True:
        try:
            choice1, choice2 = map(int, input(f"Type the two points which Player {x} wants to join: ").split())
            if choice1+1 == choice2 and logic[0][choice1-11] == "   ":
                logic[0][choice1-11] = "---"
                return choice1,choice2
            elif choice1+a == choice2 and logic[1][choice1-11] == "     ":
                logic[1][choice1-11] = "|    "
                return choice1,choice2
            else:
                print("Wrong input") 
        except ValueError:
            print("Invalid input. Please enter two valid integers separated by a space.")
        
        except IndexError:
            print("Out of bounds! Please select points that are within the grid.")
          
                 

def gamelogic(logic,wins,a):
    while True:
        while True:
            choice1, choice2 = joininggrid(a,logic,1)
            z = victor(logic,1,a,choice1,choice2)
            grid(a,logic)
            if z:
                wins[0] += 1
            else:
                break    
            if logic[0].count("---") + logic[1].count("|    ") + logic[1].count("|  1 ") + logic[1].count("|  2 ") == (a-1)*(a)*2:
                return
        while True:
            choice1, choice2 = joininggrid(a,logic,2)
            z = victor(logic,2,a,choice1,choice2)
            grid(a,logic)
            if z:
                wins[1] += 1
            else:
                break    
            if logic[0].count("---") + logic[1].count("|    ") + logic[1].count("|  1 ") + logic[1].count("|  2 ") == (a-1)*(a)*2:
                return

def victor(logic,player,a,choice1,choice2):
    z = False
    if choice1 + 1 == choice2:
        if logic[1][choice1-11] == "|    " and (logic[1][choice1-10] == "|    " or logic[1][choice1-10] == "|  1 " or logic[1][choice1-10] == "|  2 ") and logic[0][choice1-11+a] == "---":
            if player == 1:
                logic[1][choice1-11] = "|  1 "
                z = True
            elif player == 2:
                logic[1][choice1-11] = "|  2 " 
                z = True 
        if logic[0][choice1-11-a] == "---" and (logic[1][choice1-11-a] == "|    " or logic[1][choice1-11-a] == "|  1 " or logic[1][choice1-11-a] == "|  2 ") and (logic[1][choice1-10-a] == "|    " or logic[1][choice1-10-a] == "|  1 " or logic[1][choice1-10-a] == "|  2 "):
            if player == 1:
                logic[1][choice1-11-a] = "|  1 "
                z = True
            elif player == 2:
                logic[1][choice1-11-a] = "|  2 " 
                z = True
    elif choice1 + a == choice2:
        if logic[0][choice1-11] == "---" and logic[0][choice1-11+a] == "---" and (logic[1][choice1-10] == "|    " or logic[1][choice1-10] == "|  1 " or logic[1][choice1-10] == "|  2 "):
            if player == 1:
                logic[1][choice1-11] = "|  1 "
                z = True
            elif player == 2:
                logic[1][choice1-11] = "|  2 " 
                z = True 
        if logic[0][choice1-12] == "---" and logic[0][choice1-12+a] == "---" and logic[1][choice1-12] == "|    ":
            if player == 1:
                logic[1][choice1-12] = "|  1 "
                z = True
            elif player == 2:
                logic[1][choice1-12] = "|  2 " 
                z = True        
    return z   

def main():
    a = 0
    while a>8 or a<3:
        print("Please pick between 3 and 8")
        a = int(input("How many lines of pattern do you want: "))    
    prlgap = []
    prdgap = []
    for x in range(a*a):
        prlgap.append("   ")
        prdgap.append("     ")
    logic = [prlgap,prdgap]    
    grid(a,logic) 
    print("eg: 11 12 or 11 16")
    wins = [0,0]
    gamelogic(logic,wins,a)     
    if wins[0]>wins[1]:
        print("----PLAYER 1 WINS----")
    elif wins[0]<wins[1]:
        print("----PLAYER 2 WINS----")
    else:
        print("!!A TIE!!")    

main()


