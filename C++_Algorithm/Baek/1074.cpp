#include <iostream>
#include <cmath>

using namespace std;

int N, R, C;
int cnt;

void Z(int size, int y, int x)
{
	if (size == 2)
	{
		if (y == R && x == C)
		{
			cout << cnt << "\n";
			return;
		}
		cnt++;
		if (y == R && x + 1 == C)
		{
			cout << cnt << "\n";
			return;
		}
		cnt++;
		if (y + 1 == R && x == C)
		{
			cout << cnt << "\n";
			return;
		}
		cnt++;
		if (y + 1 == R && x + 1 == C)
		{
			cout << cnt << "\n";
			return;
		}
		cnt++;
		return;
	}
	Z(size / 2, y, x);
	Z(size / 2, y, x + size / 2);
	Z(size / 2, y + size / 2, x);
	Z(size / 2, y + size / 2, x + size / 2);

}



int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> R >> C;
	int q = pow(2, N);
	Z(q, 0, 0);
	return 0;

}