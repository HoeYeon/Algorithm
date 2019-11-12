#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
int gcd(int a, int b)
{
	int temp;
	if (a < b)
	{
		temp = a;
		int a = b;
		int b = temp;
	}
	while (b != 0)
	{
		temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}
int main()
{
	int n;
	cin >> n;
	int *arr = new int[n];
	int *brr = new int[n];
	map<pair<int, int>, int>mp;
	for (int i = 0; i<n; i++)
		cin >> arr[i];
	for (int i = 0; i<n; i++)
		cin >> brr[i];
	int ans = 0, cnt = 0;
	for (int i = 0; i<n; i++)
	{
		if (arr[i] == 0 && brr[i] == 0)
		{
			cnt++;
			continue;
		}
		else if (arr[i] == 0 && brr[i] != 0)
			continue;
		if (arr[i] < 0)
		{
			arr[i] *= -1;
			brr[i] *= -1;
		}
		int g = gcd(abs(arr[i]), abs(brr[i]));
		arr[i] /= g;
		brr[i] /= g;
		mp[make_pair(brr[i], arr[i])]++;
		ans = max(ans, mp[make_pair(brr[i], arr[i])]);
	}
	cout << ans + cnt << "\n";
	return 0;
}