/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

By Soleil Vivero
08/25/23

Solutions:
    1. Have another for-loop inside of the character for-loop that goes through past sections of the string..? (O(n^2))
    2. Don't clear everything in the map, just those characters that came before the char with a duplicate (O(n))
*/

#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

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

int main()
{
    Solution s;
    std::string str = "cornycab";

    std::cout << s.lengthOfLongestSubstring(str) << " <-- Result" << std::endl;
}
