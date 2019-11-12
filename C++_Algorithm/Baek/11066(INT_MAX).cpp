#include <iostream>
#include <algorithm>
#include <climits> // INT_MAX ��밡��

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
		int dp[501][501]{ 0, }; // dp[i][j] = i���� j���� �������� �ּҰ� if(i==j) dp[i][i] = 0
		int page[501];
		cin >> K;
		for (int i = 1; i <= K; i++)
		{
			cin >> page[i];
			sum[i] = sum[i - 1] + page[i];
		}
		for (int i = 1; i <= K; i++) // �� ������ ���Ҳ���
		{
			for (int j = 1; j + i <= K; j++) // n ������ 1���� k���� ��ȯ
			{
				int temp = j + i;
				dp[j][temp] = INT_MAX;
				for (int k = j; k + 1 <= temp; k++) // ���� �ӿ��� �� �ּڰ��� ��� ���س�����. if ���� ũ�Ⱑ 5��� 1,1 2,5 -> 1,2 3,5 ...�̷������� ��
					dp[j][temp] = min(dp[j][temp], dp[j][k] + dp[k + 1][temp] + sum[temp] - sum[j - 1]);
			}
		}
		cout << dp[1][K] << endl;
	}
	
	return 0;

}