#include <iostream>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

int check[1001];
vector<pair<int,int>> v[1001];
priority_queue<pair<int, int>> p;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N, M;
	cin >> N >> M;
	memset(check, 0, sizeof(check));
	for (int i = 0; i < M; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back({ c,b });
		v[b].push_back({ c, a });
	}
	int count = 0;
	p.push({0, 1});
	while (!p.empty())
	{
		int cost = -p.top().first;
		int node = p.top().second;
		p.pop();
		if (check[node] == 1)
			continue;
		check[node] = 1;
		count += cost;
		for (int i = 0; i < v[node].size(); i++)
		{
			int ccost = v[node][i].first;
			int nnode = v[node][i].second;
			p.push({ -ccost,nnode });
		}
	}
	cout << count << "\n";
	return 0;
}