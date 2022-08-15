#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

// Definition for a Node.

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

/* 
push first node in queue, 
clone it in a map if already not there, push its neighbour in queue if already not cloned.
set neighbours
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node == NULL)
            return node;
        queue <Node*> q;
        unordered_map <Node*, Node*> m;
        
        q.push(node);
        while(!q.empty()){
            Node* temp = q.front();
            q.pop();
            if(m.find(temp) == m.end()){
                Node* newNode = new Node(temp->val);
                m[temp] = newNode;
                for(auto n : temp->neighbors){
                    if(m.find(n) == m.end())
                        q.push(n);
                }
            }
        }
        for(auto nodeset : m){
            for(auto neighbor : nodeset.first->neighbors){
                nodeset.second->neighbors.push_back(m[neighbor]);
            }
        }
        return m[node];
    }
};
