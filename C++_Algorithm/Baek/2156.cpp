#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int n;
	int dp[10001] = { 0, };
	int cup[10001] = { 0, };
	int max_num = -1;

	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> cup[i];
	
	dp[1] = cup[1];
	dp[2] = cup[2] + cup[1];
	dp[3] = max(max(cup[1] + cup[3], cup[2] + cup[3]),dp[2]);

	for (int i = 4; i <= n; i++)
	 	dp[i] = max(max(cup[i] + cup[i - 1] + dp[i - 3], cup[i] + dp[i - 2]),cup[i]+cup[i-1]+dp[i-4]);

	for (int i = 1; i <= n; i++)
	{
		if (max_num < dp[i])
			max_num = dp[i];
	}
	cout << max_num << endl;
	return 0;

}