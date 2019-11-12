#include<iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int n;
	int s, result;
	cin >> n;

	cin >> s;
	result = s;
	for (int i = 1; i < n; i++)
	{
		int a;
		cin >> a;
		if (a < 0)
			result = max(result, s);
		if (s < 0 && a > s)
			s = 0;
		s += a;
		result = max(result, s);
	}
	cout << result << "\n";
	return 0;
}