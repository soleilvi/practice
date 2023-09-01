/*
https://leetcode.com/problems/add-two-numbers/

By Soleil Vivero
02/08/23
*/

/*
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
        ListNode* result;
        std::stack<int> reversedResult;
        int remainder;
        int op1;
        int op2;

        while (l1 != nullptr || l2 != nullptr)  // End when the larger list reaches its end
        {
            // If a list hasreached its end, simulate its node value being 0
            l1 == nullptr ? op1 = 0 : op1 = l1->val;
            l2 == nullptr ? op2 = 0 : op2 = l2->val;

            int sum = op1 + op2 + remainder;

            // Set remainder
            if (sum >= 10)
            {
                remainder = 1;
                sum -= 10;
            }
            else
            {
                remainder = 0;
            }

            reversedResult.push(sum);

            // Traverse lists
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;

            // If there is still a remainder at the end of both lists, add it to the result
            if (l1 == nullptr && l2 == nullptr && remainder == 1) reversedResult.push(remainder);
        }

        // Put the result in another list with the correct order
        while (!reversedResult.empty())
        {
            result = new ListNode(reversedResult.top(), result);
            reversedResult.pop();
        }

        return result;
    }
};