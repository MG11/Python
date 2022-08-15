

/* 
take queue to store node and level,
while inserting children, increment level by 1.
*/

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<pair<TreeNode*, int>> Q;
        vector<vector<int>> v;
        
        if(root == NULL){
            return v;
        }
        Q.push({root, 1});
        
        while(!Q.empty()){
            pair <TreeNode*, int> p = Q.front();
            Q.pop();
            if(p.first->left) Q.push({p.first->left, p.second + 1});
            if(p.first->right) Q.push({p.first->right, p.second + 1});
            if(p.second != v.size())
                v.push_back({});
            v[p.second -1].push_back(p.first->val);
        }
        return v;
    }
};
