/**
 * Definition for singly-linked list.

 */
#include <iostream>

  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

// https://www.youtube.com/watch?v=LCRGV8avvUY

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode* temp = head;
        while(temp && count <k){
            temp = temp->next;
            count++;
        }
        
        if(count == k){
            count = 0;
            temp = head;
            ListNode* prev= NULL;
            ListNode* next = NULL;
            while(temp && count < k){
                next = temp->next;
                temp->next = prev;
                prev = temp;
                temp = next;
                count++;
            }
            head->next = reverseKGroup(next, k);
            if(!prev)prev=head;
            return prev;
        }else
            return head;
    }
};
