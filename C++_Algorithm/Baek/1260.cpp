#include <iostream>
#include <queue>
using namespace std;

int arr[1001][1001] = { 0, };
int check[1001] = { 0, };
void dfs(int num,int N)
{
	check[num] = 1;
	cout << num << " ";
	for (int i = 1; i <= N; i++)
	{
		if(check[i] == 0 && arr[num][i] == 1)
			dfs(i,N);
	}
}
void bfs(queue<int> q,int N)
{
	while (!q.empty())
	{
		int a = q.front();
		q.pop();
		cout << a << " ";
		check[a] = 1;
		for (int i = 1; i <= N; i++)
		{
			if (check[i] == 0 && arr[a][i] == 1)
			{
				q.push(i);
				check[i] = 1;
			}
		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N, M, V;
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		arr[a][b] = 1;
		arr[b][a] = 1;
	}
	dfs(V,N);
	cout << "\n";
	for (int i = 1; i < 1001; i++)
		check[i] = 0;
	queue<int> q;
	q.push(V);
	bfs(q, N);
	return 0;
}