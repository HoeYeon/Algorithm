#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n, k;
	cin >> n >> k;
	int remain = n - 1;
	int tot = 1;
	int count = 2;
	while (true)
	{
		if (tot - remain == k)
			break;
		tot += count;
		count++;
		remain--;
	}
	cout << remain << endl;
	return 0;
}