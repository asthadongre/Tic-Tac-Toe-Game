board=["-","-","-",
       "-","-","-",
       "-","-","-",]

current_user="x"  #first user is x

gameisgoing=True

winner=None #initialies

def display_board():
    
    
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
    
    
def swipe_user():
    global current_user

    if current_user=="x":
        current_user="o"
    elif current_user=="o":
        current_user="x"
        
def row_check():
    global gameisgoing
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    if row1 or row2 or row3:
        gameisgoing=False
    if row1:
        return board[2]
    elif row2:
        return board[5]
    elif row3:
        return board[8]
        
def column_check():
    global gameisgoing
    col1=board[0]==board[3]==board[6]!="-"
    col2=board[1]==board[4]==board[7]!="-"
    col3=board[2]==board[5]==board[8]!="-"
    if col1 or col2 or col3:
        gameisgoing=False
    if col1:
        return board[6]
    elif col2:
        return board[7]
    elif col3:
        return board[8]
        
def digonal():
    global gameisgoing
    dig1=board[0]==board[4]==board[8]!="-"
    dig2=board[2]==board[4]==board[6]!="-"
    if dig1 or dig2:
        gameisgoing=False
    if dig1:
        return board[8]
    elif dig2:
        return board[6]
            
def check_draw():
    count=0    
    global gameisgoing 
    for i in range(9):
        if board[i]=="x" or board[i]=="o":
             count+=1
            
        if count==9:
            print("the game is drawn!!")
            gameisgoing = False
                  
def winner():
    global winner
    
    col_winner=column_check() 
    row_winner=row_check()
    dig_winner=digonal()
    check_draw()
    
    if col_winner:
        winner=col_winner
    elif row_winner:
        winner=row_winner
    elif dig_winner:
        winner=dig_winner
    
def handle_turn():
    global current_user
    try:
        position=int(input("Enter the position (0-8): "))
        board[position]=current_user
        display_board()
         
    except:
        print("Enter between 0-8")
        return handle_turn()
            
def play_game():
    global gameisgoing
    display_board()
    
    while gameisgoing:
        handle_turn()
        swipe_user()
        winner()
        
    if winner=="x":
        print("Winner is First player!!")
    elif winner=="o":
        print("Winner is second player!!")
        
play_game()


