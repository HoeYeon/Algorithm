#include <iostream>
#include <algorithm>

using namespace std;

long long arr[2000001] = { 0, };
int main()
{
	arr[0] = 0;
	arr[1] = 1;
	arr[2000000] = 1;
	arr[1999999] = -1;
	for (int i = 2; i <= 1000000; i++)
		arr[i] = (arr[i - 1]%1000000000 + arr[i - 2] % 1000000000)% 1000000000;
	for (int i = 1999998; i > 1000000; i--)
	{
		if (arr[i + 2] < 0)
			arr[i + 2] = -1 * (abs(arr[i + 2]) % 1000000000);
		else
			arr[i+2] = arr[i + 2] % 1000000000;

		if(arr[i+1] < 0)
			arr[i+1] = -1*(abs(arr[i + 1]) % 1000000000);
		else
			arr[i + 1] = arr[i + 1] % 1000000000;
		arr[i] = (arr[i + 2] - arr[i + 1]) % 1000000000;
	}
	int N;
	cin >> N;
	if (N < 0)
		N += 2000001;
	if (arr[N] < 0)
		cout << -1 << "\n";
	else if (arr[N] == 0)
		cout << 0 << "\n";
	else
		cout << 1 << "\n";
	cout << abs(arr[N]) << "\n";
	return 0;
}