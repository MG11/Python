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

// todo do it by O(n) time complexity
class Solution {
public:
    int heightOfTree(TreeNode* root){
        if(root == NULL)
            return 0;
        
        return max(heightOfTree(root->left), heightOfTree(root->right)) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        if(root == NULL)
            return 0;
        
        int lheight = heightOfTree(root->left);
        int rheight = heightOfTree(root->right);
        int ldiameter = diameterOfBinaryTree(root->left);
        int rdiameter = diameterOfBinaryTree(root->right);
        /*
            Return max of the following tree:
            1) Diameter of left subtree
            2) Diameter of right subtree
            3) Height of left subtree + height of right subtree +1
        */
        cout <<lheight << " "<<rheight<<" "<<ldiameter<<" "<<rdiameter<<endl;
        
        return max((lheight + rheight), max(ldiameter, rdiameter));
        
    }
};
