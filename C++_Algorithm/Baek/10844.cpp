#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	long long arr[10][101] = { 0, };
	int N;
	cin >> N;
	arr[1][0] = 1;
	for (int i = 0; i < 10; i++)
		arr[i][1] = 1;
	for (int i = 2; i < 101; i++)
	{
		for (int j = 1; j < 10; j++)
		{
			if (j == 1)
				arr[j][i] = (arr[j][i - 2] + arr[j + 1][i - 1])%1000000000;
			else if (j == 9)
				arr[j][i] = arr[j - 1][i - 1];
			else
				arr[j][i] = (arr[j - 1][i - 1] + arr[j + 1][i - 1]) % 1000000000;
		}
	}
	long long result = 0;
	for (int i = 1; i < 10; i++)
	{
		result += arr[i][N];
		result = result % 1000000000;
	}
	cout << result << "\n";

	return 0;
}