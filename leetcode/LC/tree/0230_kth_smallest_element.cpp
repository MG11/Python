#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

 // Definition for a binary tree node.
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
 
class Solution {
    
    int kthSmallestHepler(TreeNode* root, int& k) {
        if(root == NULL)
            return -1;
        int val = kthSmallestHepler(root->left, k);
        if(val != -1)return val;
        
        if(k == 1)
            return root->val;
        k--;
        
        val = kthSmallestHepler(root->right, k);
        if(val != -1)return val;
        return -1;
    }
    
public:
    int kthSmallest(TreeNode* root, int k) {
        if(root == NULL)
            return -1;
        return kthSmallestHepler(root, k);
    }
};
