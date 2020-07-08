import random,time
board=[[6,0,0,1,0,0,0,0,2],[8,0,1,0,9,0,0,0,0],[0,7,5,0,8,4,0,0,0],[4,3,0,0,2,0,5,6,1],[5,1,8,7,0,0,4,0,9],[0,9,6,4,1,0,3,0,0],[0,0,0,0,7,0,0,0,0],[0,6,0,0,3,1,0,5,0],[7,0,2,5,4,0,6,0,3]]

def display(board):
	#global board
        print("="*33)
        for i in board:
                if i==board[3] or i==board[6]:
                        print("-"*33)
                
                print(i[0:3],i[3:6],i[6:],sep=" | ")
                
        print("="*33)


def isValidSudoku(board,row,col,n):
		#global board
		for i in range(9):
			if board[row][i]==n or board[i][col]==n:
				return False

		row//=3
		row*=3
		col//=3
		col*=3
		for i in range(row,row+3):
			for j in range(col,col+3):
				if board[i][j]==n:
					return False


		return True

def solve(board,row,col):
	#global board
	#display()

	if(row==9):
		print("Solution :")
		display(board)
		return True
	if col==9:
		return solve(board,row+1,0)

	if board[row][col]!=0:
		return solve(board,row,col+1)

	for i in range(9):
		if isValidSudoku(board,row,col,i+1):
			board[row][col]=i+1
			x=solve(board,row,col+1)
			if x:
				return True
	board[row][col]=0
	return False


def newsuduko():
	board=[[0 for i in range(9)]for i in range(9)]
	num=random.randint(25,30)
	for i in range(0,num):

		x=random.randint(0,8)
		y=random.randint(0,8)
		val=random.randint(1,9)
		if isValidSudoku(board,x,y,val):
			board[x][y]=val
		else:
			i-=2
	return board


print("QUESTION:")
#display(board)

#ch=input("Press 1 to countinue\nPress 2 for new Sudoku :")
ch=input("Press 1 to generate a new suduko puzzle \nPress 2 to continue \nPress 3 to enter your own sudoku ")
if(ch=='1'):
        new=newsuduko()
        print("New Sudoku:=>")
        display(new)
        print("\n\nHarsh is trying to solve your puzzle-----")
        #time.sleep(1.5)
        print()
        x=solve(new,0,0)
        if x==False:
                print("Suduko was not valid--->Try Again")
elif(ch=='2'):
	print("Sudoku is: ")
	display(board)
	print("\n\n")
	solve(board,0,0)
else:
        print("="*10+"Welcome"+"="*10)
        print("Enter your sudoku row wise (1 row at a time) & for blank spaces enter '0'")
        newboard=[]
        for i in range(9):
                if i%3==0:print("\n")
                l=list(map(int,input("Enter one row with space seperated integers ").split()))
                newboard.append(l)
        print("\n\nThis is your entered sudoku->\n")
        display(newboard)
        print("\n\nHarsh is trying to solve your puzzle-----")
        x=solve(newboard,0,0)
        if x==False:
                print("Suduko was not valid--->Try Again")
                
        

