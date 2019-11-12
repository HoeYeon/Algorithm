#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N;
	cin >> N;
	int v[10001] = { 0, };
	for (int i = 0; i < N; i++)
	{
		int a;
		cin >> a;
		v[a]++;
	}
	for (int i = 0; i < 10001; i++)
		if (v[i] > 0)
		{
			for (int j = 0; j < v[i]; j++)
				cout << i << "\n";
		}
	return 0;
}