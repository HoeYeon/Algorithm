#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int N, M;
	int degree[32001] = { 0, };
	int a, b, count=0;
	vector<int> v[32001];
	queue<int> q;
	cin >> N >> M;
	for (int i = 0; i < M; i++)
	{
		cin >> a >> b;
		degree[b]++;
		v[a].push_back(b);
	}
	while (count != N)
	{
		for (int i = 1; i <= N; i++)
		{
			if (degree[i] == 0)
			{
				q.push(i);
				cout << i << " ";
				degree[i] = -1;
				count++;
			}
		}
		while (!q.empty())
		{
			int t = q.front();
			q.pop();
			for (int i = 0; i < v[t].size(); i++)
				degree[v[t][i]]--;
		}
	}
	cout << "\n";
	return 0;
}