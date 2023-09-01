/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

By Soleil Vivero
08/26/23
*/

#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> charMap;
        int longestSubstringLength = 0;
        int charIndex = 0;
        int keyValue = 0;

        // Iterate through string characters
        for (auto &ch : s)
        {
            // Check for duplicates
            if (charMap.contains(ch))
            {
                keyValue = charMap.at(ch);

                // Erase the duplicate along with any character that came before it
                for (auto it = charMap.begin(); it != charMap.end();)
                {
                    if (it->second <= keyValue)
                    {
                        it = charMap.erase(it);
                    }
                    else
                    {
                        it++;
                    }
                }
            }

            charMap.insert({ch, charIndex++});

            // Update the size of the longest substring if needed
            if (charMap.size() > longestSubstringLength)
            {
                longestSubstringLength = charMap.size();
            }
        }

        return longestSubstringLength;
    }
};
