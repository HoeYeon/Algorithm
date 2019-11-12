#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int arr[100000] = { 0, };
	for (int i = 2; i < 100000; i++)
	{
		if (arr[i] == 0)
		{
			for (int j = i * 2; j < 100000; j += i)
				arr[j] = 1;
		}
	}
	int T;
	cin >> T;
	while (T--)
	{
		int arr2[100000] = { 0, };
		int N;
		cin >> N;
		int i = 2;
		while(N != 1)
		{
			for (i; i < 100000; i++)
			{
				if (arr[i] ==0 && N%i == 0)
					break;
			}
			arr2[i]++;
			N /= i;
		}
		for (int i = 2; i < 100000; i++)
		{
			if(arr2[i] != 0)
				cout << i << " " << arr2[i] << "\n";
		}
	}
	return 0;
}