#include <iostream>

using namespace std;

//int num[10001] = { 0, };
int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int N;
		int count = 0;
		int arr[100];
		int num[10001] = { 0, };
		cin >> N;
		for (int j = 0; j < N; j++)
			cin >> arr[j];
		num[0] = 1;
		for (int j = 0; j < N; j++)
		{
			for (int k = 10000; k >=0; k--)
			{
				if (num[k] == 1 && k + arr[j] < 10000)
					num[k + arr[j]] = 1;
			}
		}
		for (int j = 0; j < 10001; j++)
		{
			if (num[j] == 1)
				count++;
		}
		cout << "#" << i << " " << count << "\n";
	}
	return 0;
}