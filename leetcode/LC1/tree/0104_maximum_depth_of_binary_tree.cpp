#include <iostream>
#include <vector>
#include <queue>
using namespace std;


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
    int maxDepth(TreeNode* root) {
        if(!root)
            return 0;
        
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

/* 
if left and right depth both are present, then take minimum of them else take depth
which is present.
*/
// minimum depth
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        
        int leftdepth = minDepth(root->left);
        int rightdepth = minDepth(root->right);
        
        if(leftdepth && rightdepth)
            return 1 + min(leftdepth, rightdepth);
        else
            return 1 + max(leftdepth, rightdepth);
    }
};