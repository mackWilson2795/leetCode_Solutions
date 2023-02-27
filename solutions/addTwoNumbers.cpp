/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int r = 0, s = 0;
        ListNode* sum = new ListNode();
        ListNode* nx = sum;
        while(l1 || l2 || r ) {
            s = 0;
            if (l1){
                s += l1->val;
                l1 = l1->next;
            }
            if (l2){
                s += l2->val;
                l2 = l2->next;
            }
            s += r;
            r = s / 10;
            s = s % 10;
            nx->val = s;
            if (l1 || l2 || r ){
                nx->next = new ListNode();
                nx = nx->next;
            }
        }
        nx = NULL;
        return sum;
    }
};