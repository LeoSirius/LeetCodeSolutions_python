#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int res = 0;
        int start = 0;
        int end = 1;
        // start 和 end 左闭右开
        while (end < nums.size()) {
            int max_reach = 0;
            for (int i = start; i < end; i++) {
                max_reach = max(max_reach, nums[i] + i);
            }
            start = end;        // 下一次起跳点范围开始的格子
            end = max_reach + 1;    // 下一次起跳点范围结束的格子
            ++res;
        }
        return res;
    }
};

void test(string test_name, vector<int>& nums, int expected)
{
    int res = Solution().jump(nums);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {2,3,1,1,4};
    int expected1 = 2;
    test("test1", nums1, expected1);

    return 0;
}
