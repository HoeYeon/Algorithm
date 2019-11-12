#include <iostream>

using namespace std;

int arr[505][505];
int dp[505][505];
int N, M;

int xx[4] = { 0,1,0,-1 };
int yy[4] = { 1,0,-1,0 };
int dfs(int x, int y)
{
	if (dp[x][y] != -1)
		return dp[x][y];
	if (x == M && y == N)
		return 1;
	dp[x][y] = 0;
	for (int i = 0; i < 4; i++)
	{
		if (arr[x][y] > arr[x + xx[i]][y + yy[i]])
			dp[x][y] += dfs(x + xx[i], y + yy[i]);
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

	cout << dfs(1,1) << "\n";

	return 0;
}