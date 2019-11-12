#include <iostream>

using namespace std;

long long coun[1000001] = { 0, };
void getdiv()
{
	for (int i = 1; i <= 1000000; i++)
	{
		for (int j = 1; j <= 1000000 / i; j++)
			coun[i*j] += i;
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T, N;
	cin >> T;
	getdiv();
	for (int i = 2; i <= 1000000; i++)
		coun[i] += coun[i - 1];
	for (int i = 0; i < T; i++)
	{
		cin >> N;
		cout << coun[N] << "\n";
	}
	return 0;
}