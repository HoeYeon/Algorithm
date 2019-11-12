#include <iostream>

using namespace std;

int arr[1001] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n, k;
	cin >> n >> k;
	int count = 0;
	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		arr[a]++;
		if (arr[a] == 2)
		{
			count++;
			arr[a] = 0;
		}
	}
	if (n % 2 == 1)
		n++;
	int sets = n / 2;
	int result = count * 2 + sets - count;
	cout << result << endl;
}