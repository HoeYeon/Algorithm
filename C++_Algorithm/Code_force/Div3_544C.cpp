#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int arr[200000] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n, maxx = 1;
	cin >> n;
	vector <int> v;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr, arr + n);
	v.push_back(arr[0]);

	for (int i = 1; i < n; i++)
	{
		while (v.size() > 0 && arr[i] - v[0] > 5)
			v.erase(v.begin());
		v.push_back(arr[i]);
		if (maxx < v.size())
			maxx = v.size();
	}
	cout << maxx << "\n";
	return 0;
}