/**
 * Definition for a binary tree node.
 
 */
/* 
take two stacks push root in s1.
push elements in s2 stack in left to right (maintains even level)
push elements in s1 stack in right to left (maintains odd level)
*/

#include <climits>
#include <iostream>
using namespace std;
#include <vector>
#include <stack>

 struct TreeNode {
      int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        
        vector<vector<int>> v;
    
        if(root == NULL){
            return v;
        }
        stack<TreeNode*> s1;
        stack<TreeNode*> s2;
        s1.push(root);
        vector<int> dummy;
        
        while(!s1.empty() || !s2.empty()){
            dummy = {};
            while(!s1.empty()){
                TreeNode* node = s1.top();
                dummy.push_back(node->val);
                s1.pop();
                if(node->left)s2.push(node->left);
                if(node->right)s2.push(node->right);
            }
            if(dummy.size()) v.push_back(dummy);
            dummy = {};
            while(!s2.empty()){
                TreeNode* node = s2.top();
                dummy.push_back(node->val);
                s2.pop();
                if(node->right)s1.push(node->right);
                if(node->left)s1.push(node->left);
            }
            if(dummy.size()) v.push_back(dummy);
        }
        return v;
    }
};
