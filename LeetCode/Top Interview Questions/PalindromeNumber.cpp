/*
https://leetcode.com/problems/palindrome-number/

By Soleil Vivero
Conversion algorithm from https://math.stackexchange.com/questions/480068/how-to-reverse-digits-of-an-integer-mathematically
08/18/23
*/

#include <cmath>
#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) 
    {
        if (x < 0)
        {
            return false;
        }

        float logx = std::round(std::log10(x));
        std::cout << "logx: " << logx << std::endl;
        float factorsSum = 0;
        float factor1 = 0;
        float factor2 = 0;
        float result = 0;

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

        result = std::round(x * std::pow(10, logx) - 99 * factorsSum);  // calculation reverses order of digits in x
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