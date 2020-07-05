#include<iostream>
using namespace std;

void display(int board[9][9])
{
    cout<<"DISPLAY\n";
	for(int i=0;i<9;i++)
      {
         for(int j=0;j<9;j++)
			cout<<board[i][j]<<" ";
		cout<<endl;
      }
}

bool isvalid(int board[9][9],int row,int col,int val)
{
	for(int i=0;i<9;i++)
		if(board[i][col]==val or board[row][i]==val)
			return false;
    row/=3;
    row*=3;
    col/=3;
    col*=3;
	for(int i=row;i<row+3;i++)
		{for(int j=col;j<col+3;j++)
			if(board[i][j]==val)
				return false;

		}
	return true;

}

bool isPossible(int mat[9][9],int row,int col,int num){

	for(int i=0;i<9;i++){
		if(mat[row][i]==num or mat[i][col]==num){
			return false;
		}
	}

	int starting_x = (row/3)*3;
	int starting_y = (col/3)*3;

	for(int i = starting_x;i<starting_x+3;i++){
		for(int j=starting_y;j<starting_y+3;j++){
			if(mat[i][j]==num){
				return false;
			}
		}
	}

	return true;
}


bool solve(int board[9][9],int row,int col)
{
    //cout<<row<<endl;
	if(row==9)
	{
	    cout<<"done\n";
		display(board);
		return true;
	}
	if(col==9)
		return solve(board,row+1,0);

	if(board[row][col]!=0)
		return solve(board,row,col+1);

	for(int i=1;i<=9;i++)
	{
		if(isvalid(board,row,col,i))
		{
			board[row][col]=i;
			bool next=solve(board,row,col+1);
			if(next)
				return true;
		}
	}
	board[row][col]=0;
	return false;

}

int main()
{

	int mat[9][9] = {
            {5,3,0,0,7,0,0,0,0},
            {6,0,0,1,9,5,0,0,0},
            {0,9,8,0,0,0,0,6,0},
            {8,0,0,0,6,0,0,0,3},
            {4,0,0,8,0,3,0,0,1},
            {7,0,0,0,2,0,0,0,6},
            {0,6,0,0,0,0,2,8,0},
            {0,0,0,4,1,9,0,0,5},
            {0,0,0,0,8,0,0,7,9}
    };
    display(mat);
    cout<<"===========================================\n";
    cout<<solve(mat,0,0);
	return 0;
}
