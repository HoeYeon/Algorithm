#include <iostream>

using namespace std;

int main() {
	
	long long dp[101] = { 0, };
	int T, N;
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;
	for (int i = 6; i <= 100; i++)
	{
		dp[i] = dp[i - 1] + dp[i - 5];
	}
	cin >> T;
	while (T--)
	{
		cin >> N;
		cout << dp[N] << endl;
	}


	return 0;
}