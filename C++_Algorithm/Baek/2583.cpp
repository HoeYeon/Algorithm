#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int mat[100][100] = { 0, };
int check[100][100] = { 0, };
int mov[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int M, N, K; // M = «‡, N = ø≠
	cin >> M >> N >> K;
	queue <pair<int,int>> q;
	vector <int> v; // ≥–¿Ã
	int count = 0;

	for (int i = 0; i < K; i++)
	{
		int x1, x2, y1, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int j = y1; j < y2; j++)
		{
			for (int k = x1; k < x2; k++)
				mat[j][k] = 1;
		}
	}
	/*for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
			cout << mat[i][j] << " ";
		cout << endl;
	}*/
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			int num = 0;
			if (check[i][j] == 0 && mat[i][j] == 0)
			{
				q.push(make_pair(i, j));
				check[i][j] = 1;
				num++;
			}
			while (!q.empty())
			{
				int xx = q.front().first;
				int yy = q.front().second;
				q.pop();
				for (int k = 0; k < 4; k++)
				{
					int x = mov[k][0];
					int y = mov[k][1];
					if (x + xx >= 0 && x + xx < M && y + yy >= 0 && y + yy < N)
					{
						if (mat[xx + x][yy + y] == 0 && check[xx + x][yy + y] == 0)
						{
							q.push(make_pair(xx + x, yy + y));
							check[xx + x][yy + y] = 1;
							num++;
						}
					}
				}
			}
			if (num >= 1)
			{
				v.push_back(num);
				count++;
			}
		}
	}
	sort(v.begin(), v.end());
	cout << count << "\n";
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	return 0;
}