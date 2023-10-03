#include <iostream>
#include <cstring>

using namespace std;
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int dp[N + 1];
    memset(dp, 0, sizeof(dp));

    int nums[N];
    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];
    }

    int lis = 0;
    for (int i = 0; i < N; i++)
    {
        int val = nums[i];
        dp[val] = dp[val - 1] + 1;
        lis = max(lis, dp[val]);
    }

    cout << N - lis << endl;

    return 0;
}