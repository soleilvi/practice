/*
https://leetcode.com/problems/palindrome-number/

By Soleil Vivero
Conversion algorithm from https://math.stackexchange.com/questions/480068/how-to-reverse-digits-of-an-integer-mathematically
08/19/23
*/

#include <cmath>
#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) 
    {
        // A number with a negative sign will never be a palindrome
        if (x < 0)
        {
            return false;
        }
        // A single digit will always be a palindrome
        else if (x < 10)
        {
            return true;
        }

        double logx = std::round(std::log10(x));
        std::cout << "logx: " << logx << std::endl;
        double factorsSum = 0;
        double factor1 = 0;
        double factor2 = 0;
        double result = 0;

        for (int i = 1; i <= logx; i++)
        {
            factor1 = std::round(x * std::pow(10, -i));
            factor2 = std::round(std::pow(10, logx - i));
            factorsSum += factor1 * factor2;

            std::cout << "factor1 at " << i << ": "<< factor1 << std::endl;
            std::cout << "factor2 at " << i << ": "<< factor2 << std::endl;
            std::cout << "factorsSum at " << i << ": "<< factorsSum << std::endl;
            std::cout << std::endl;
        }

        result = x * std::pow(10, logx) - 99 * factorsSum;  // calculation reverses order of digits in x
        result = std::abs(std::round(result));;  // For the sake of clarity, rounding and converting to absolute value are on a different line
        std::cout << result << std::endl;

        if (static_cast<int>(result) == x)  // turn result into an integer to compare
        {
            return true;
        } 
        else
        {
            return false;
        }
    }
};

int main()
{
    int x = 88888;
    Solution solution;

    if (solution.isPalindrome(x))
    {
        std::cout << x << " is a palindrome" << std::endl;
    }
    else
    {
        std::cout << x << " is not a palindrome" << std::endl;
    }
}