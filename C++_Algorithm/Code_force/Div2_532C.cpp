#include <iostream>
#include <queue>
#include <cmath>
#include <string>

using namespace std;
int mov[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };

int arr[51][51] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	for (int i = 0; i < 51; i++)
	{
		for (int j = 0; j < 51; j++)
			arr[i][j] = -1;
	}
	int n;
	cin >> n;
	int r1, c1,r2,c2;
	int min = 9999999;
	string s;
	queue<pair<int,int>> q;
	cin >> r1 >> c1 >> r2 >> c2;
	for (int i = 1; i <= n; i++)
	{
		cin >> s;
		for (int j = 0; j < n; j++)
		{
			arr[i][j + 1] = int(s[j]-48);
		}
	}
	for (int i = 1; i < n+1; i++)
	{
		for (int j = 1; j < n+1; j++)
			cout << arr[i][j] << " ";
		cout << endl;
	}
	int visit[51][51] = { 0, };
	q.push(make_pair(r1, c1));
	visit[r1][c1] = 1;
	int x1, y1,x2,y2;
	while (!q.empty())
	{
		x1 = q.front().first;
		y1 = q.front().second;
		q.pop();
		/*int len = pow(x - r2, 2) + pow(y - c2, 2);
		if (len < min)
			min = len;*/
		for (int i = 0; i < 4; i++)
		{
			if (x1 + mov[i][0] < n + 1 && x1 + mov[i][0] >0 && y1 + mov[i][1] < n + 1 && y1 + mov[i][1] > 0)
			{
				if (arr[x1 + mov[i][0]][y1 + mov[i][1]] == 0 && visit[x1 + mov[i][0]][y1 + mov[i][1]] == 0)
				{
					q.push(make_pair(x1 + mov[i][0], y1 + mov[i][1]));
					visit[x1 + mov[i][0]][y1 + mov[i][1]] = 1;
				}
			}
		}
	}
	visit[51][51] = { 0, };
	q.push(make_pair(r2, c2));
	visit[r2][c2] = 1;
	while (!q.empty())
	{
		x2 = q.front().first;
		y2 = q.front().second;
		q.pop();
		/*int len = pow(x - r2, 2) + pow(y - c2, 2);
		if (len < min)
		min = len;*/
		for (int i = 0; i < 4; i++)
		{
			if (x2 + mov[i][0] < n + 1 && x2 + mov[i][0] >0 && y2 + mov[i][1] < n + 1 && y2 + mov[i][1] > 0)
			{
				if (arr[x2 + mov[i][0]][y2 + mov[i][1]] == 0 && visit[x2 + mov[i][0]][y2 + mov[i][1]] == 0)
				{
					q.push(make_pair(x2 + mov[i][0], y2 + mov[i][1]));
					visit[x2 + mov[i][0]][y2 + mov[i][1]] = 1;
				}
			}
		}
	}
	int len = pow(x1 - x2, 2) + pow(y1 - y2, 2);
	cout << len << "\n";
	return 0;
}