#include<iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int arr[1000001] = {0, };
	arr[1] = 1;
	int N, M;
	cin >> N >> M;

	for (int i = 2; i <= M; i++)
	{
		if (arr[i] == 0)
		{
			for (int j = i * 2; j <= M; j += i)
				arr[j] = 1;
		}
	}
	for (int i = N; i <= M; i++)
	{
		if (arr[i] == 0)
			cout << i << "\n";
	}

	return 0;
}