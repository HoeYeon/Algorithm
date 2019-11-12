#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int bb[11] = { 0, };
int N, M, up, down,a;
int len(int n)
{
	int l = 0;
	while (n != 0)
	{
		l++;
		n /= 10;
	}
	if (l == 0)
		l = 1;
	return l;
}
bool check(int n)
{
	int length = len(n);
	for (int i = 0; i < length; i++)
	{
		int temp = n % 10;
		if (bb[temp] == 1)
			return true;
		n /= 10;
	}
	return false;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M;
	for (int i = 0; i < M; i++)
	{
		cin >> a;
		bb[a] = 1;
	}
	up = N;
	while (check(up) && up<= 999999)
		up++;
	down = N;
	while (check(down) && down >= 0)
		down--;
	int one;
	if (down < 0)
		down = -99999999;
	if (abs(N - up) < abs(N - down))
		one = abs(N - up) + len(up);
	else
		one = abs(N - down) + len(down);
	
	int two = abs(100 - N);
	if (one == 0)
		one = 1;
	cout << min(one, two) << endl;
	return 0;
}

