/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

By Soleil Vivero
08/23/23

Solutions:
    1. Have another for-loop inside of the character for-loop that goes through past sections of the string..? (O(n^2))
    2. Don't clear everything in the map, just those characters that came before the char with a duplicate (O(n))
        - For auto solution: not as easy with the 
*/

#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

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
            // if (charMap.contains(ch))
            // {
            //     keyValue = charMap.at(ch);

            //     for (auto &item : charMap)
            //     {
            //         std::cout << item.first << ", " << item.second << std::endl;
            //     }
            // }

            charMap.insert({ch, charIndex});

            std::cout << "Map size: " << charMap.size() << ", Longest substring: " << longestSubstringLength << std::endl;

            if (charMap.size() > longestSubstringLength)
            {
                longestSubstringLength = charMap.size();
            }

            charIndex++;
        }

        return longestSubstringLength;
    }
};

int main()
{
    Solution s;
    std::string str = "abcabca";

    std::cout << s.lengthOfLongestSubstring(str);
}

/*
for (int i = 0; i < s.length(); i++)
{
    charMap.insert(i, s.at(i));



    if (charMap.size() > longestSubstringLength)
    {
        longestSubstringLength = charMap.size();
    }
}
*/