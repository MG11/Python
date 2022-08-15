#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//first valid all rows, then valid all columns, then valid a box.
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i< board[0].size(); i++){
            if(!is_valid_row(board, i, 0))   
                return false;
        }
        
        for(int i = 0; i< board.size(); i++){
            if(!is_valid_column(board, 0, i))   
                return false;
        }
        
        for(int i = 0; i<board[0].size(); i++){
            for(int j = 0; j<board.size(); j++){
                if(!is_valid_box(board, i, j))
                    return false;
            }
        }
        return true;
    }
    
    bool is_valid_row(vector<vector<char>>& board, int row, int col){
        unordered_set<int> s;
        for(int i = 0; i<board[0].size(); i++){
            if(board[row][i] == '.')
                continue;
            if (s.find(board[row][i]) == s.end()){
                s.insert(board[row][i]);
            }else{
                return false;
            }
                
        }
        return true;
    }
    
    
    bool is_valid_column(vector<vector<char>>& board, int row, int col){
        unordered_set<int> s;
        for(int i = 0; i<board.size(); i++){
            if(board[i][col] == '.')
                continue;
            if (s.find(board[i][col]) == s.end()){
                s.insert(board[i][col]);
            }else{
                return false;
            }
        }
        return true;
    }
    
    
    bool is_valid_box(vector<vector<char>>& board, int row, int col){
        
        int si = 3*(row/3);
        int sj = 3*(col/3);
        unordered_set<int> s;
        for(int i = si; i<si+3; i++){
            for(int j = sj; j<sj+3; j++){
                 if(board[i][j] == '.')
                    continue;                       
                 if (s.find(board[i][j]) == s.end()){
                s.insert(board[i][j]);
            }else{
                return false;
            }
            }
        }
        return true;
    }
    
};