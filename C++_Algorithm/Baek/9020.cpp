#include<iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int arr[10001] = { 0, };
	arr[1] = 1;
	int T;
	cin >> T;
	for (int i = 2; i <= 10000; i++)
	{
		if (arr[i] == 0)
		{
			for (int j = i * 2; j <= 10000; j += i)
				arr[j] = 1;
		}
	}
	while (T--)
	{
		int n;
		pair<int, int> min = make_pair(0, 999999);
		cin >> n;
		for (int i = 2; i <= n / 2; i++)
		{
			if (arr[i] == 0 && arr[n-i] == 0)
			{
				if (abs(n - i - i) < abs(min.first - min.second))
					min = make_pair(i, n - i);
			}
		}
		cout << min.first << " " << min.second << "\n";

	}

	return 0;
}