/*
https://leetcode.com/problems/longest-palindromic-substring/

By Soleil Vivero
08/28/23

Palindrome if:
    - For a string with an even number of letters, both sides are the same if split down the middle and mirrored
    - For a string with an odd number of letters, both sides are the same if you exclude the middle character and mirror the sides

So, excluding the middle character in odd-number palindromes, it is necessary for characters to repeat the same number of times in reverse order.
*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) 
    {
        // Somebody else's solution to the Longest Substring problem that I've been trying to understand:
        vector<int> charVect(128,-1);
        int left = 0;
        int strLength = s.size();
        int longestSubstringLength  = 0;
        int right = 0;

        while (right < strLength)
        {
            std::cout << "s[i]: " << s[right] << std::endl;
            std::cout << "m[s[i]]: " << charVect[s[right]] << std::endl;
            if (charVect[s[right]] != -1)  // true when there are character repeats
            {
                left = max(left, charVect[s[right]] + 1);  // Unless l was already greater, it sets l to the number of times the current character has appeared
                std::cout << "L: " << left << std::endl;
            }
            charVect[s[right]] = right;
            longestSubstringLength = max(longestSubstringLength, right - left + 1);
            right++;
        }
        return s;
    }
};