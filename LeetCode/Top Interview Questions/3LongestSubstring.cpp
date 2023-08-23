/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

By Soleil Vivero
08/23/23
*/

#include <string>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> charSet;
        int longestSubstringLength = 0;

        // Iterate through string characters
        for (auto &ch : s)
        {
            if (charSet.contains(ch))
            {
                charSet.clear();
            }

            charSet.insert(ch);
            if (charSet.size() > longestSubstringLength)
            {
                longestSubstringLength = charSet.size();
            }
        }
        return longestSubstringLength;
    }
};

int main()
{
    Solution s;
    std::string str = "Looop";

    std::cout << s.lengthOfLongestSubstring(str);
}