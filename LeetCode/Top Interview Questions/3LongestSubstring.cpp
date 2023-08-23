/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

By Soleil Vivero
08/22/23
*/

#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
        1. Parse through string
        2. If there are any, look through characters in set
        3. If the letter being parsed is not in the set, add it to the set
        4. If it is...
            a. Record how many characters are in the set
                - UNLESS a previously recorder int is greater!
            b. Empty set
            c. Add character to set
        */
        std::unordered_set<char> mySet;
    }
};