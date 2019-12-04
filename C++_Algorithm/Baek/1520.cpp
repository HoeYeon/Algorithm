#include <iostream>

using namespace std;

int arr[505][505];
long long dp[505][505];
int N, M;

int go[4][4] = { { 0,1 },{ 1,0 },{ 0,-1 },{ -1,0 } };
long long dfs(int x, int y)
{
	if (dp[x][y] != -1)
		return dp[x][y];
	if (x == M && y == N)
		return 1;
	dp[x][y] = 0;
	for (int i = 0; i < 4; i++)
	{
		if (x + go[i][0] > 0 && x + go[i][0] <= M && y + go[i][1] > 0 && y + go[i][1] <= N) {
			if (arr[x][y] > arr[x + go[i][0]][y + go[i][1]])
				dp[x][y] += dfs(x + go[i][0], y + go[i][1]);
		}
	}
	return dp[x][y];

}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	for (int i = 0; i < 505; i++)
	{
		for (int j = 0; j < 505; j++)
			dp[i][j] = -1;
	}

	cin >> M >> N;
	for (int i = 1; i <= M; i++)
	{
		for (int j = 1; j <= N; j++)
			cin >> arr[i][j];
	}

	cout << dfs(1, 1) << "\n";

	return 0;
}