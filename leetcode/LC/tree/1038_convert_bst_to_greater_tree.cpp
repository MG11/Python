#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

 /**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// do reverse inorder traversal right root left
class Solution {
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
