#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int n, k;
	int coin[101] = { 0, };
	int dp[10001] = { 0, };
	dp[0] = 1;

	cin >> n >> k;
	
	for (int i = 0; i < n; i++)
		cin >> coin[i];

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= k; j++)
		{
			if (j >= coin[i])
				dp[j] += dp[j - coin[i]];
		}
	}

	cout << dp[k] << endl;
}