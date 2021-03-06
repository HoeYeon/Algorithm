#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
int r1, c1, r2, c2;
int d[50][5];

int getNum(int x, int y)
{
	if (x >= 0 && -1 * x <= y && y <= x)
		return (x * 2 + 1)*(x * 2 + 1) - (x - y);
	else if (x<0 && x <= y && y <= abs(x))
	{
		return (abs(x) * 2)*(abs(x) * 2) - (abs(x) - 1) - y;
	}
	else if (y>x&& y>-1 * x)
	{
		return ((y - 1) * 2 + 1)* ((y - 1) * 2 + 1) + (y - x);
	}
	else
	{
		return (abs(y) * 2)*(abs(y) * 2) + (x - y + 1);
	}




	return -1;
}

int maxx = -1;

int main() {
	cin >> r1 >> c1 >> r2 >> c2;
	maxx = max(max(getNum(r1, c1), getNum(r2, c2)), max(getNum(r1, c2), getNum(r2, c1)));
	int size = to_string(maxx).size();

	for (int i = r1; i <= r2; i++)
	{
		for (int j = c1; j <= c2; j++)
		{
			printf("%*d ", size, getNum(i, j));
		}
		cout << endl;
	}

	return 0;
}