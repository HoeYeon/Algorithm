#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int sum[10001] = { 0, };

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int arr[10001] = { 0, };
	vector <pair<int, int>> v; // ½Â,ÆÐ
	int n,check = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr, arr+n);
	for (int i = 0; i < n; i++)
		v.push_back(make_pair(arr[i], n - 1 - arr[i]));
	for (int i = 0; i < n-1; i++)
	{
		if (v[i].first < 0 || v[i].second < 0)
			break;
		int j = i + 1;
		for (j; v[i].first-- > 0; j++)
			v[j].second--;
		for (j; v[i].second-- > 0; j++)
			v[j].first--;
	}
	if (v[n - 1].first == 0 && v[n - 1].second == 0)
		cout << 1 << "\n";
	else
		cout << -1 << "\n";
	return 0;
}