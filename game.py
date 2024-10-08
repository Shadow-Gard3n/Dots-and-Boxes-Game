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
        choice1, choice2 = map(int, input(f"Type the two points which Player {x} wants to join: ").split())
        if choice1+1 == choice2 and logic[0][choice1-11] == "   ":
            logic[0][choice1-11] = "---"
            return logic
        elif choice1+a == choice2 and logic[1][choice1-11] == "     ":
            logic[1][choice1-11] = "|    "
            return logic
        else:
            print("Wrong input")    

def gamelogic(logic,wins,a):
    while True:
        while True:
            joininggrid(a,logic,1)
            z = victor(logic,1,a)
            grid(a,logic)
            if z == True:
                wins[0] += 1
            elif z == False:
                break    
            if logic[0].count("---") + logic[1].count("|    ") + logic[1].count("|  1 ") + logic[1].count("|  2 ") == (a-1)*(a)*2:
                return
        while True:
            joininggrid(a,logic,2)
            z = victor(logic,2,a)
            grid(a,logic)
            if z == True:
                wins[1] += 1
            elif z == False:
                break    
            if logic[0].count("---") + logic[1].count("|    ") + logic[1].count("|  1 ") + logic[1].count("|  2 ") == (a-1)*(a)*2:
                return

def victor(logic,player,a):
    z = False
    for x in range(0,a*a):
        if logic[0][x] == "---" and (logic[1][x] == "|    " or logic[1][x] == "|  1 " or logic[1][x] == "|  2 ") and (logic[1][x+1] == "|    " or logic[1][x+1] == "|  1 " or logic[1][x+1] == "|  2 ") and logic[0][x+a] == "---" and player == 1:
            logic[1][x] = "|  1 "
            z = True
        elif logic[0][x] == "---" and (logic[1][x] == "|    " or logic[1][x] == "|  1 " or logic[1][x] == "|  2 ") and (logic[1][x+1] == "|    " or logic[1][x+1] == "|  1 " or logic[1][x+1] == "|  2 ") and logic[0][x+a] == "---" and player == 2:
            logic[1][x] = "|  2 " 
            z = True         
    return z   
           
def main():
    a = 0
    while a>8 or a<3:
        print("Please pick between 8 and 3")
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


