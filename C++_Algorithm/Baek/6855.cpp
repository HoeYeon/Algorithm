#include<iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T, N, K;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> N >> K;
		vector <int> v;
		vector <int> d;
		int a, sum = 0;
		for (int j = 0; j < N; j++)
		{
			cin >> a;
			v.push_back(a);
		}
		for (int j = 1; j < N; j++)
		{
			d.push_back(v[j] - v[j - 1]);
		}
		sort(d.begin(), d.end());
		if (K <= N)
		{
			for (int j = 0; j < d.size() - (K - 1); j++)
				sum += d[j];
		}
		else
			sum = 0;
		cout << "#" << i << " " << sum << "\n";
	}
}