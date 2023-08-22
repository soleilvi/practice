/*
https://leetcode.com/problems/palindrome-number/

By Soleil Vivero
08/21/23
*/

class Solution {
public:
    bool isPalindrome(int x) 
    {
        // A number with a negative sign will never be a palindrome
        if (x < 0)
        {
            return false;
        }

        long xReversed = 0;
        int xLastNum = 0;
        int xCopy = x;

        for (int i = 0; xCopy != 0; i++)
        {
            // Get last digit in x
            xLastNum = xCopy % 10;

            // Add the digit to the reversed version of x in the correct place value
            xReversed *= 10;
            xReversed += xLastNum;

            // Remove the digit from "x"
            xCopy -= xLastNum;
            if (xCopy != 0)
            {
                xCopy /= 10;
            }
        }

        if (xReversed == x)
        {
            return true;
        } 
        else
        {
            return false;
        }
    }
};