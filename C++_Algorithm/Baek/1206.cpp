#include <iostream>
#include <algorithm>
using namespace std;

int b[1001];
int check(int i)
{
	return min(min(b[i] - b[i - 1], b[i] - b[i - 2]), min(b[i] - b[i + 1], b[i] - b[i + 2]));
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	for (int i = 0; i < 10; i++)
	{
		b[1001] = { 0, };
		int N;
		int count = 0;
		cin >> N;
		for (int j = 1; j <= N;j++)
			cin >> b[j];
		for (int j = 3; j <= N - 2; j++)
		{
			if (check(j) > 0)
				count += check(j);
		}
		cout <<"#" << i+1 << " " << count << "\n";
	}
	return 0;
}