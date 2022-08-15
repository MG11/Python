#include <climits>
#include <iostream>
using namespace std;
#include <vector>

struct TreeNode {
      int val;
     TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/* 

LC 1448
pass max possible by value and store result in reference..
*/
class Solution {
public:
    void goodNodesHelper(TreeNode* root, int &res, int max){
        if(root == NULL)
            return;
        if(root->val >= max){
            res++;
            max = root->val;
        }
        goodNodesHelper(root->left, res, max);
        goodNodesHelper(root->right, res, max);
        
    }
    int goodNodes(TreeNode* root) {
        int res = 0;
        goodNodesHelper(root, res, INT_MIN);
        return res;
    }
};
