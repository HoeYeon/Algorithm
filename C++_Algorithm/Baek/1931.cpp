#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const pair<long long, long long> &p1, const pair<long long, long long> &p2) {
	if (p1.second < p2.second) {
		return true;
	}
	else if (p1.second == p2.second)
		return p1.first < p2.first;
	else {
		return false;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N;
	vector<pair<long long, long long>> v;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		long long a, b;
		cin >> a >> b;
		v.push_back({ a,b });
	}
	/*sort(v.begin(), v.end());

	
	cout << endl;
	for (int i = 0; i < N; i++)
		cout << v[i].first << " " << v[i].second << endl;
	cout << endl;
	*/
	sort(v.begin(), v.end(), cmp);
	/*cout << endl;
	for (int i = 0; i < N; i++)
		cout << v[i].first << " " << v[i].second << endl;
	cout << endl;*/

	long long start = v[0].first, end = v[0].second;
	int count = 1;
	for (int i = 1; i < N; i++)
	{
		if (v[i].first < end)
			continue;
		count++;
		start = v[i].first;
		end = v[i].second;
	}

	cout << count << endl;

	return 0;
}