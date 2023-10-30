// BOJ 2533. 사회망 서비스(SNS)

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> adj[1000001];
int dp[1000001][2];
bool visited[1000001];




int dfs(int cur, int parent, int state) {
    int& ret = dp[cur][state];
    if (ret != -1) return ret;
    visited[cur] = true;
    if (state == 1) {
        ret = 1;
        for (int next : adj[cur]) {
            if (next == parent) continue;
            ret += min(dfs(next, cur, 0), dfs(next, cur, 1));
        }
    }
    else {
        ret = 0;
        for (int next : adj[cur]) {
            if (next == parent) continue;
            ret += dfs(next, cur, 1);
        }
    }
    visited[cur] = false;
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> N;
    for (int i = 0; i < N - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    fill(&dp[0][0], &dp[1000000][2], -1);
    cout << min(dfs(1, 0, 0), dfs(1, 0, 1));
    return 0;
}