#include <iostream>

using namespace std;



int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;
	int arr[101][101];
	long long dp[101][101] = { 0, };
	int N;
	int c = 0;

	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
			cin >> arr[i][j];
	}
	dp[1][1] = 1;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (arr[i][j] == 0 || dp[i][j] ==0)
				continue;
			if(j + arr[i][j] <= N)
				dp[i][j + arr[i][j]] += dp[i][j];
			if(i + arr[i][j] <= N)
				dp[i + arr[i][j]][j] += dp[i][j];
		}
	}
	
	cout << dp[N][N] << "\n";
	return 0;

}