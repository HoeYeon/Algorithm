#include <iostream>

using namespace std;
int arr[501][501] = { 0, };
int check[501] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	for (int i = 0; i <= 500; i++)
		arr[i][i] = 1;
	int a, b, n, m,count=0;
	cin >> n >> m;
	while (m--)
	{
		cin >> a >> b;
		arr[a][b] = 1;
		arr[b][a] = 1;
	}
	for (int i = 2; i <= n; i++)
	{
		if (arr[1][i] != 0)
		{
			for (int j = 2; j <= n; j++)
			{
				if (arr[i][j] != 0 && check[j] == 0)
				{
					count++; check[j] = 1;
				}
			}
		}
	}
	cout << count << endl;
	return 0;
}