/**
 * Definition for singly-linked list.

 */

//https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8843/C%2B%2B-solution-easy-to-understand-with-explanations.

#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* removeNthFromEnd2(ListNode* head, int n) {
        int listLength = 0;
        ListNode* temp = head;
        while(temp){
            temp = temp->next;
            listLength++;
        }
        int nodePosition = listLength - n - 1;
        if(nodePosition <0){
            head = head->next;
            return head;
        }
        temp = head;
        for(int i = 0; i<nodePosition; i++){
            temp = temp->next;
        }
        temp->next = temp->next->next;
        return head;
    }
    
    // without calculating length
    // O(n)
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(-1);
        ListNode* slow = dummy;
        ListNode* fast = dummy;
        dummy->next = head;
        int count = n;
        
        while(n--){
            fast = fast->next;
        }
        while(fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};
