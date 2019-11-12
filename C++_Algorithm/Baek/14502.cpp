#include <iostream>
#include <queue>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int go[4][4] = { {1,0},{0,1},{-1,0},{0,-1} };
int arr[8][8];
int check[8][8] = { 0, };
int N, M;
int mmax = -1;
queue<pair<int, int>> qq;
vector<pair<int, int>> v;

int find_max()
{
	int arr2[8][8] = { 0, };
	int check2[8][8];
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			arr2[i][j] = arr[i][j];
			check2[i][j] = check[i][j];
		}
	}
	queue<pair<int, int>> q;
	q = qq;


	while (!q.empty())
	{
		int f = q.front().first;
		int s = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int x = f + go[i][0];
			int y = s + go[i][1];
			if (x >= 0 && x < N && y >= 0 && y < M)
			{
				if (check2[x][y] == 0 && arr2[x][y] == 0)
				{
					check2[x][y] = 1;
					arr2[x][y] = 2;
					q.push({ x,y });
				}
			}
		}
	}
	int result = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (arr2[i][j] == 0)
				result++;
		}
	}
	return result;
}
void permute(vector<pair<int,int>> vv)
{
	if (vv.size() == 3)
	{
		mmax = max(mmax, find_max());
		return;
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (arr[i][j] == 0)
			{
				arr[i][j] = 1;
				vv.push_back({ i,j });
				permute(vv);
				arr[i][j] = 0;
				vv.pop_back();
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> arr[i][j];
			if (arr[i][j] == 2)
			{
				qq.push({ i,j });
				check[i][j] = 1;
			}
		}
	}
	
	permute(v);
	cout << mmax << endl;

}