/*
https://leetcode.com/problems/two-sum/

By Soleil Vivero
01/19/2023
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> operands;
        int op1, op2;

        for (int i = 0; i < nums.size(); i++)
        {
            op1 = nums.at(i);
            for (int j = 0; j < nums.size(); j++)
            {
                op2 = nums.at(j);
                if ((op1 + op2 == target) && (i != j))
                {
                    operands.push_back(i);
                    operands.push_back(j);
                    return operands;
                }
            }
        }

        return operands;
    }
};