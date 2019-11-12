#include <iostream>

using namespace std;
int mat[1000002] = { 0, }; //0 is top, 1000001 is bot
int sz[1000002] = { 0, };
int id[1001][1001];
int root(int p)
{
	while (p != mat[p])
	{
		mat[p] = mat[mat[p]];
		p = mat[p];
		cout << p << " " << mat[p] << endl;
	}
	return p;
}
void uni(int p, int q)
{
	if (id[p][q] != 0)
		return;
	int i = root(p);
	int j = root(q);

	if (sz[i] < sz[j])
	{
		mat[i] = j; 
		sz[i] += sz[j];
	}
	else
	{
		mat[j] = i;
		sz[j] += sz[i];
	}
}

bool connected(int p, int q)
{
	int i = root(p);
	int j = root(q);
	if (i == j)
		return true;
	else
		return false;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int M, N;

	cin >> M >> N;

	for (int i = 1; i <= M; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> id[i][j];
			sz[(i - 1)*N + j]++;
			mat[(i - 1)*N + j] = (i - 1)*N + j;
		}
	}
	cout << "QWE" << endl;
	for (int i = 1; i <= M; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (id[i][j] == 0)
			{
				if (i == 1)
				{
					mat[(i - 1)*N + j] = 0;
					sz[0]++;
				}
				else if (i == M)
				{
					mat[(i - 1)*N + j] = 1000001;
					sz[1000001]++;
				}
				else if (j == 1)
				{
					uni((i - 1)*N + j, (i - 2)*N + j);
					uni((i - 1)*N + j, i*N + j);
					uni((i - 1)*N + j, (i - 1)*N + j+1);
				}
				else if (j == N)
				{
					uni((i - 1)*N + j, (i - 2)*N + j);
					uni((i - 1)*N + j, i*N + j);
					uni((i - 1)*N + j, (i - 1)*N + j - 1);
				}
				else
				{
					uni((i - 1)*N + j, (i - 2)*N + j);
					uni((i - 1)*N + j, i*N + j);
					uni((i - 1)*N + j, (i - 1)*N + j - 1);
					uni((i - 1)*N + j, (i - 1)*N + j + 1);
				}
			}
		}
	}

	cout << boolalpha << connected(0, 1000001) << endl;

	return 0;
}