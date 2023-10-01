#include <iostream>
#include <cstring>
using namespace std;

int main(void)
{
    int T;
    cin >> T;

    while (T > 0)
    {
        T -= 1;
        int N;
        cin >> N;
        int A[N];

        for (int i = 0; i < N; i++)
            cin >> A[i];

        int dp[N][N];
        memset(dp, 0, sizeof(dp));

        bool turn = (N % 2) == 1;
        for (int size = 0; size < N; size++)
        {
            for (int i = 0; i < N - size; i++)
            {
                if (size == 0)
                    dp[i][i + size] = turn ? A[i] : 0;
                else if (turn)
                    dp[i][i + size] = max(dp[i + 1][i + size] + A[i], dp[i][i + size - 1] + A[i + size]);
                else
                    dp[i][i + size] = min(dp[i + 1][i + size], dp[i][i + size - 1]);
            }
            turn = !turn;
        }

        cout << dp[0][N - 1] << endl;
    }

    return 0;
}