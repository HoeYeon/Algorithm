#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T, N;
	cin >> T;
	for (int k = 0; k < T; k++)
	{
		cin >> N;
		vector<pair<int, int>> v;
		for (int i = 0; i < N; i++)
		{
			int a, b;
			cin >> a >> b;
			v.push_back({ a,b });
		}
		sort(v.begin(), v.end());
		int maxx = v[0].second;
		int count = 1;
		for (int i = 1; i < N; i++)
		{
			if (v[i].second < maxx)
			{
				maxx = v[i].second;
				count++;
			}
		}
		cout << count << "\n";
	}
	return 0;
}