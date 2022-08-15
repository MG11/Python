// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1#
 // } Driver Code Ends
class Solution{

	public:
	int canPartition(int nums[],int n, const int &target, int sum){
        vector <int> arr(target+1, 0);
        arr[0] = 1;
        for(int i = 0; i < n; i++){
            for(int j = target; j>=0; j--){
                if(arr[j] && j + nums[i] <= target){
                    arr[j + nums[i]] += 1;
                }
            }
        }
        return arr[sum];
    }
    
	int perfectSum(int arr[], int n, int sum)
	{
        // Your code goes here
        int target = 0;
        for(int i = 0; i<n; i++){
            target += arr[i];
        }
        return canPartition(arr,n,target, sum);
	}
	  
};

// { Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n, sum;

        cin >> n >> sum;

        int a[n];
        for(int i = 0; i < n; i++)
        	cin >> a[i];

       

	    Solution ob;
	    cout << ob.perfectSum(a, n, sum) << "\n";
	     
    }
    return 0;
}
  // } Driver Code Ends
  