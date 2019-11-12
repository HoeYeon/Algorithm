#include <iostream>
#include <algorithm>
#include <climits> // INT_MAX 사용가능

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T, K;
	
	cin >> T;

	while (T--)
	{
		int sum[501] = { 0, };
		int dp[501][501]{ 0, }; // dp[i][j] = i부터 j까지 묶었을때 최소값 if(i==j) dp[i][i] = 0
		int page[501];
		cin >> K;
		for (int i = 1; i <= K; i++)
		{
			cin >> page[i];
			sum[i] = sum[i - 1] + page[i];
		}
		for (int i = 1; i <= K; i++) // 몇 묶음씩 비교할껀지
		{
			for (int j = 1; j + i <= K; j++) // n 묶음씩 1부터 k까지 순환
			{
				int temp = j + i;
				dp[j][temp] = INT_MAX;
				for (int k = j; k + 1 <= temp; k++) // 묶음 속에서 또 최솟값을 계속 구해나간다. if 묶음 크기가 5라면 1,1 2,5 -> 1,2 3,5 ...이런식으로 비교
					dp[j][temp] = min(dp[j][temp], dp[j][k] + dp[k + 1][temp] + sum[temp] - sum[j - 1]);
			}
		}
		cout << dp[1][K] << endl;
	}
	
	return 0;

}