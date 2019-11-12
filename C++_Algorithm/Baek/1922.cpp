#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int arr[1001][1001];
int check[1001];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N, M;
	cin >> N >> M;
	memset(arr, 10001, sizeof(arr));
	memset(check, 0, sizeof(check));
	vector<int> v;
	for (int i = 0; i < M; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		arr[a][b] = c;
		arr[b][a] = c;
	}
	v.push_back(1);
	check[1] = 1;
	int count = 0;
	while (v.size() != N)
	{
		int min = 10001;
		int temp = -1;
		for (int i = 0; i < v.size(); i++)
		{
			for (int j = 1; j <= N; j++)
			{
				if (check[j] == 0 && arr[v[i]][j] < min)
				{
					min = arr[v[i]][j];
					temp = j;
				}
			}
		}
		check[temp] = 1;
		v.push_back(temp);
		count += min;
	}

	cout << count << endl;
	return 0;
}