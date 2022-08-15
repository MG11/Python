#include <iostream>
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == NULL && q == NULL)
            return true;
        if(p == NULL || q == NULL)
            return false;
        if(p->val == q->val){
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
        return false;
    }
};

// https://leetcode.com/problems/sum-of-left-leaves/
class Solution2 {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root){
             return 0;
         }
        int countvalue = 0;
        if(root->left && !root->left->left && !root->left->right){
            countvalue = root->left->val;
        }
        return  countvalue + sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);   
    }
};

// https://leetcode.com/problems/insert-into-a-binary-search-tree/
class Solution3 {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root == NULL){
            TreeNode* node = new TreeNode(val);
            return node;
        }
        if(val < root->val)
            root->left = insertIntoBST(root->left, val);
        else
            root->right = insertIntoBST(root->right, val);
        return root;
    }
};