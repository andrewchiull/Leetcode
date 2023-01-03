/*
520. Detect Capital
https://leetcode.com/problems/detect-capital/description/

@ Easy
@ String

We define the usage of capitals in a word to be right when one of the following cases holds:

- All letters in this word are capitals, like `"USA"`.
- All letters in this word are not capitals, like `"leetcode"`.
- Only the first letter in this word is capital, like `"Google"`.

Given a string `word`, return `true` if the usage of capitals in it is right.
*/

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        int countUpper = 0;
        int size = word.size();
        for (size_t i = 0; i < word.size(); i++)
        {
            if (isupper(word[i])) countUpper++;
        }
        if (countUpper == 0 || countUpper == word.size())
            return true;

        return true;
    }
};

int main() {
    string word = "woAw";
    
    Solution sol;
    bool res = sol.detectCapitalUse(word);
    cout << res << '\n';
    return 0;
}