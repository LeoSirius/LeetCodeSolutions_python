#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        // p 表示列号。对每一列，遍历所有字符串
        for(int p = 0; strs.size()>0; prefix += strs[0][p++]){
            for(int i = 0; i < strs.size(); ++i){
                // p已经走到了最短那个字符串的尽头 or
                // p列有字符不同， 则返回
                if(p >= strs[i].size() || (i > 0 && strs[i][p] != strs[i-1][p]))
                    return prefix;
            }
        }
        return prefix;
    }
};

int main(){
    Solution s = Solution();
    vector<string> input;
    input.push_back("");
    input.push_back("");
    string res = s.longestCommonPrefix(input);
    cout << res << endl;
}