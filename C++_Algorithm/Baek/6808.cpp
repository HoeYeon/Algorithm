#include <iostream>

using namespace std;

int TC[9];
int check[19];
int score1;
int score2;
int result1;
int result2;
int check2[9];
void dfs(int n)
{
	if (n == 9)
	{
		if (score1 > score2)
			result1++;
		else if (score2 > score1)
			result2++;
		return;
	}
	else 
	{
		for (int i = 0; i < 9; i++)
		{
			if (check[check2[i]] == 0)
			{
				check[check2[i]] = 1;
				if (TC[n] > check2[i])
					score1 += (TC[n] + check2[i]);
				else if (check2[i] > TC[n])
					score2 += (TC[n] + check2[i]);
				dfs(n + 1);
				check[check2[i]] = 0;
				if (TC[n] > check2[i])
					score1 -= (TC[n] + check2[i]);
				else if (check2[i] > TC[n])
					score2 -= (TC[n] + check2[i]);
			}
		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin >> T;
	for (int k = 1; k <= T; k++)
	{
		result1 = 0;
		result2 = 0;
		memset(check, 0, sizeof(check));
		for (int i = 0; i < 9; i++)
		{
			cin >> TC[i];
			check[TC[i]] = 1;
		}
		int temp = 0;
		for (int i = 1; i < 19; i++)
		{
			if (check[i] == 0)
			{
				cout << i << " ";
				check2[temp] = i;
				temp++;
			}
		}
		dfs(0);
		cout <<"#" << k << " " << result1 << " " << result2 << "\n";
	}
	return 0;
}