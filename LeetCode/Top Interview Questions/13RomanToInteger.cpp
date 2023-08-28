/*
https://leetcode.com/problems/roman-to-integer/

By Soleil Vivero
08/27/23
*/

class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        bool modI = false, modX = false, modC = false;  // For when I, X, or C act as modifiers for another integer

        // Iterate through string chars
        for (auto &ch : s)
        {
            switch (ch)
            {
                case 'I':
                    result++;
                    modI = true;
                    break;
                case 'V':
                    result += modI ? 3 : 5;  // 3 instead of 4 since I has already been added
                    modI = false;
                    break;
                case 'X':
                    result += modI ? 8 : 10;
                    modI = false;
                    modX = true;
                    break;
                case 'L':
                    result += modX ? 30 : 50;
                    modX = false;
                    break;
                case 'C':
                    result += modX ? 80 : 100;
                    modX = false;
                    modC = true;
                    break;
                case 'D':
                    result += modC ? 300 : 500;
                    modC = false;
                    break;
                case 'M':
                    result += modC ? 800 : 1000;
                    modC = false;
                    break;
            }
        }
        return result;
    }
};