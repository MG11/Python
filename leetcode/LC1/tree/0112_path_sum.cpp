#include <unordered_set>
#include <vector>
using namespace std;

  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

// https://leetcode.com/problems/path-sum/
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root == NULL)
            return false;
        if(targetSum == root->val && !root->left && !root->right)
            return true;
        
        bool leftside = hasPathSum(root->left, targetSum - root->val);
        if(leftside)
            return leftside;
        bool rightside = hasPathSum(root->right, targetSum - root->val);
        return rightside;
    }
};

// https://leetcode.com/problems/path-sum-ii/

class Solution2 {
    void pathSumHelper(TreeNode* root, int targetSum, vector<int> &p, vector<vector<int>> &result) {
        if(!root)return;
        p.push_back(root->val);
        if(root->val == targetSum && !root->left && !root->right){
            result.push_back(p);
        }
        pathSumHelper(root->left, targetSum - root->val, p, result);
        pathSumHelper(root->right, targetSum - root->val, p, result);
        p.pop_back();
        return;
    }
    
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if(root == NULL)
            return {};
        vector<int> path;
        vector<vector<int>> result;
        pathSumHelper(root, targetSum, path, result);
        return result;
    }
};

