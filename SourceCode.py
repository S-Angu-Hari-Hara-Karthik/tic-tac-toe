from IPython.display import clear_output
def display(b):
    clear_output()
    print(" "+b[7]+" | "+b[8]+" | "+b[9])
    print("-----------")
    print(" "+b[4]+" | "+b[5]+" | "+b[6])
    print("-----------")
    print(" "+b[1]+" | "+b[2]+" | "+b[3])
def mark(b,sp,pos):
    b[pos]=sp;
def checkspace(b,pos):
    return b[pos]==" "
def chooseposition(b,p):
    pos=0
    while pos not in [1,2,3,4,5,6,7,8,9] or not checkspace(b,pos):
        pos=int(input(p+" Choose your position[1-9] "))
    return pos;
def checkwin(b,sp):
    if(b[7]==sp and b[8]==sp and b[9]==sp) or (b[4]==sp and b[5]==sp and b[6]==sp)or (b[1]==sp and b[2]==sp and b[3]==sp)or (b[7]==sp and b[4]==sp and b[1]==sp)or (b[8]==sp and b[5]==sp and b[2]==sp)or (b[9]==sp and b[6]==sp and b[3]==sp)or (b[7]==sp and b[5]==sp and b[3]==sp)or (b[9]==sp and b[5]==sp and b[1]==sp):
        return 1
    else:
        return 0;
def draw(b):
    for i in range(1,10):
        if b[i] ==' ':
            return 0
    return 1

while(True):
    print("Welcome To Tic Tac Toe")
    display(['z','1','2','3','4','5','6','7','8','9'])
    p1=input("enter name of player1 ").strip().upper()
    p2=input("enter name of player2 ").strip().upper()
    print(p1,"Enter a symbol=",end=" ")
    sp1=input().strip().upper()
    print(p2,"Enter a symbol=",end=" ")
    sp2=input().strip().upper()
    xxx=0
    while(sp1==sp2):
        if xxx>4:
            print("Game ends")
            exit(0)
        xxx+=1
        print(p2,"Enter different symbol",end=" ")
        sp2=input().strip().upper()

    m=input(p1+" do you want to start first?(yes or no)").upper()
    if m[0]=='Y':
        turn=p1;
    else:
        turn=p2;
    print("GAME ON")
    game=True
    b=[' ']*10;
    while game:
        if turn==p1:
            display(b)
            pos=chooseposition(b,p1)
            mark(b,sp1,pos)
            if checkwin(b,sp1):
                display(b)
                print("Congrats "+p1+" won the match")
                break
            else:
                if draw(b):
                    print("Draw Match")
                    break;
                else:
                    turn=p2
        else:
            display(b)
            pos=chooseposition(b,p2)
            mark(b,sp2,pos)
            if checkwin(b,sp2):
                display(b)
                print("Congrats "+p2+" won the match")
                break
            else:
                if draw(b):
                    print("Draw Match")
                    break
                else:
                    turn=p1
    again=input("Do you want to play again(yes or no)").strip().upper()
    if again[0]=='N':
        break;

        

 
