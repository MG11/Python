#include <climits>
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

 class TreeNode {
     public:
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
 
class Solution {
    vector<int> ans;
    void inorderTraversalHelper(TreeNode* root){
        if(root == NULL){
            return;
        }
        inorderTraversalHelper(root->left);
        ans.push_back(root->val);
        inorderTraversalHelper(root->right);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        inorderTraversalHelper(root);
        return ans;
    }
};

//https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


// do reverse inorder traversal right root left
class Solution2 {
    void bstToGst(TreeNode* root, int& sum){
        if(root == NULL){
            return;
        }
        bstToGst(root->right, sum);
        int val = root->val;
        root->val += sum;
        sum += val;
        bstToGst(root->left, sum);
        return;
    }
public:
    TreeNode* bstToGst(TreeNode* root) {
        int sum = 0;
        bstToGst(root, sum);
        return root;
    }
};
