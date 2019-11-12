#include <iostream>
#include <algorithm>

using namespace std;


int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;

	int dp[301], stair[301];
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++)
		cin >> stair[i];

	dp[1] = stair[1];
	dp[2] = max(stair[1] + stair[2], stair[2]);
	dp[3] = max(stair[1] + stair[3], stair[2] + stair[3]);

	for (int i = 4; i <= N; i++)
	{
		dp[i] = max((stair[i] + stair[i - 1] + dp[i - 3]), (stair[i] + dp[i - 2]));
	}

	cout << dp[N] << endl << endl;


	return 0;

}