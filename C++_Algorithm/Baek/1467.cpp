#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int a,b,c;
	cin >> a >> b >> c;
	int N = 1;
	while (true)
	{
		if ((N-1) % 15 + 1 == a && (N - 1) % 28 +1 == b && (N - 1) % 19+1 == c)
			break;
		N++;
	}
	cout << N << "\n";
	return 0;
}