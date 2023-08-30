/*
https://leetcode.com/problems/longest-palindromic-substring/

By Soleil Vivero
08/28/23

Palindrome if:
    - For a string with an even number of letters, both sides are the same if split down the middle and mirrored
    - For a string with an odd number of letters, both sides are the same if you exclude the middle character and mirror the sides

So, excluding the middle character in odd-number palindromes, it is necessary for characters to repeat the same number of times in reverse order.

For this:
    1. Iterate through string
    2. At each character, divide its index by 2
*/

#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) 
    {
        vector<int> v(128,-1);
        std::string longestPalindrome = "";
        
        for (int i = 0; i < std::round(s.length()/2); i++)
        {
        //     v.at(s.at(i)) = i;

        //     for (int j = i; j > -1; j--)
        //     {
        //         int x = std::round(j / 2);

                
        //     }
        }

        return longestPalindrome;
    }
};

int main()
{
    std:vector<int> v(10, 0);
    
    for (auto &u : v)
    {
        std::cout << u << std::endl;
    }
}

/*
// Somebody else's solution to the Longest Substring problem that I've been trying to understand:
vector<int> charVect(128,-1);  // Initiate a vector with 128 -1s
int left = 0;
int strLength = s.size();
int longestSubstringLength  = 0;
int curCharIndex = 0;

while (curCharIndex < strLength)
{
    std::cout << "s[i]: " << s[curCharIndex] << std::endl;
    std::cout << "m[s[i]]: " << charVect[s[curCharIndex]] << std::endl;
    if (charVect[s[curCharIndex]] != -1)  // true when there are character repeats
    {
        left = max(left, charVect[s[curCharIndex]] + 1);  // Unless l was already greater, it sets l to the number of times the current character has appeared
        std::cout << "L: " << left << std::endl;
    }
    charVect[s[curCharIndex]] = curCharIndex;
    longestSubstringLength = max(longestSubstringLength, curCharIndex - left + 1);
    curCharIndex++;
}
return longestSubstringLength;
*/