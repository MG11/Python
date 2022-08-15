#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

//https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/?category[]=Dynamic%20Programming&category[]=Dynamic%20Programming&page=4&query=category[]Dynamic%20Programmingpage4category[]Dynamic%20Programming#

class Solution{   
public:
    bool isSubsetSum(int N, int arr[], int sum){
        // code here 
        bool t[N+1][sum+1];
        
        // base case
        for(int i = 0; i<=N;i++){
            for(int j = 0; j <=sum; j++){
                if(i == 0)t[i][j] = false; // if array size is 0 we can't create sum
                if(j == 0)t[i][j] = true; // if sum is 0 we can create sum any time
            }
        }
        
        for(int i = 1; i<= N; i++){ // arr size
            for(int j = 1; j <= sum; j++){ // sum
                if(arr[i-1] <=j)
                    // if value is less than current sum
                    t[i][j] = t[i-1][j] || t[i-1][j - arr[i-1]];
                else
                    // if value is greater than current sum
                    t[i][j] = t[i-1][j];
            }
        }
        for (int i = 0; i <= N; i++)
     {
       for (int j = 0; j <= sum; j++)
          printf ("%4d", t[i][j]);
       printf("\n");
     }
        return t[N][sum];
        
    }
};
