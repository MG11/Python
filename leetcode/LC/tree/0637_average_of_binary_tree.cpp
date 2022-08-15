/**
do level order traversal and maintain store sum
O(n) | O(n)
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
    vector<double> averageOfLevels(TreeNode* root) {
        vector <double> v;
        if(root == NULL)
            return v;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){
            double s = q.size();
            double temp = 0.0;
            
            for(int i = 0; i< s; i++){
                TreeNode* node = q.front();
                temp += node->val;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                q.pop();
            }
            cout<< temp <<" "<<s<<endl;
            v.push_back((temp/s));
        }
        return v;
    }
};
