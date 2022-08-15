/*
// Definition for a Node.

*/
#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

/*
take left and right as DDL prev and next, do inorder traversal and keep track of
 prev node, after recursion join prev and head.
*/

class Solution {
public:
    Node* prev = nullptr;
    Node* head = nullptr;
    void treeToDoublyListHelper(Node* root) {
        if(root == nullptr)
            return;
        treeToDoublyListHelper(root->left);
        if(!prev){ 
            head = root;
        }else{
            root->left = prev;
            prev->right = root;
        }
        prev = root;
        treeToDoublyListHelper(root->right);
    }
    
    Node* treeToDoublyList(Node* root) {
        treeToDoublyListHelper(root);
        if(head){
            head->left = prev;
            prev->right = head;
        }
        return head;
    }
};
