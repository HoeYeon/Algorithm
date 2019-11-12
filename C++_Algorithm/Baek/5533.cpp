#include<iostream>

using namespace std;

int main()
{
	int arr[101][3] = { 0, };
	int man[200][3] = { 0, };
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			int a;
			cin >> a;
			man[i][j] = a;
			if (arr[a][j] == 0)
				arr[a][j] = 1;
			else if (arr[a][j] == 1)
				arr[a][j] = -1;
		}
		
	}
	for (int i = 0; i < N; i++)
	{
		int sum = 0;
		for (int j = 0; j < 3; j++)
		{
			if (arr[man[i][j]][j] == 1)
				sum += man[i][j];
		}
		cout << sum << "\n";
	}
	return 0;
}