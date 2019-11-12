#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
int dd[100] = { 0, };
int v[200000] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n, k,a,count=0;
	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		v[i] = a % k;
	}
	//sort(v, v+n);
	for (int i = 0; i < n; i++)
		dd[v[i]]++;
	count += dd[0] / 2;
	for (int i = 1; i < ceil(double(k) / double(2)); i++)
		count += min(dd[i], dd[k - i]);

	if (k % 2 == 0)
		count += dd[k / 2] / 2;
	cout << count * 2 << "\n";
	return 0;
}