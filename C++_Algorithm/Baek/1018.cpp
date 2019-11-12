#include <iostream>
#include <stack>

using namespace std;
char ch[8][8] = {
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
};
char ch2[8][8] = {
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	char chess[50][50];
	int min= 3000;
	int N, M;

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
			cin >> chess[i][j];
	}
		
	for (int i = 0; i <= N - 8; i++)
	{
		for (int j = 0; j <= M - 8; j++)
		{
			int count = 0;
			int num1 = 0, num2 = 0;

			for (int q = i; q < 8 + i; q++)
			{
				for (int w = j; w < 8 + j; w++)
				{
					if (chess[q][w] != ch[q-i][w-j])
						num1++;
					if (chess[q][w] != ch2[q - i][w - j])
						num2++;
				}

			}
			if (num1 < num2)
				count = num1;
			else
				count = num2;
			if (count< min)
				min = count;
		}
	}
	cout << min;
	return 0;
}