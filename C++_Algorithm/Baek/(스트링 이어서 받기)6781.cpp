#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	while (T--)
	{
		int card[3][10] = { 0, };
		int temp[9];
		int count = 0;
		string s;
		for (int i = 0; i < 9; i++)
			scanf_s("%1d", &temp[i]);
		cin >> s;
		for (int i = 0; i < 9; i++)
		{
			if (s[i] == 'R')
				card[0][temp[i]]++;
			else if (s[i] == 'G')
				card[1][temp[i]]++;
			else
				card[2][temp[i]]++;
		}
		for (int i = 0; i < 3; i++)
		{
			for (int j = 1; j < 10; j++)
			{
				if (card[i][j] / 3 > 0)
				{
					count += card[i][j] / 3;
					card[i][j] = card[i][j]%3;
				}
			}
			for (int j = 1; j < 8; j++)
			{
				int a = min(card[i][j], min(card[i][j + 1], card[i][j + 2]));
				count += a;
				card[i][j] -= a;
				card[i][j + 1] -= a;
				card[i][j + 2] -= a;
			}
		}
		cout << "#" << 5 - T;
		if (count >= 3)
			cout << " Win\n";
		else
			cout << " Continue\n";
	}
	return 0;
}