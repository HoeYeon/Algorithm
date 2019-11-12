#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	long long  arr[100001][2] = { 0, };
	arr[0][0] = 1;
	arr[0][1] = 1;
	int n;
	long long count = 0;
	cin >> n;
	for (int i = 1; i <= 2*n; i++)
	{
		int a;
		cin >> a;
		if (arr[a][0] == 0)
			arr[a][0] = i;
		else
			arr[a][1] = i;
	}
	for (int i = 0; i < n; i++)
		count += abs(arr[i][0] - arr[i + 1][0]) + abs(arr[i][1] - arr[i + 1][1]);
	cout << count << "\n";
	return 0;
}