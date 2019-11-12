#include <iostream>
#include <cmath>
using namespace std;

int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	long long a, b;
	long long r = 0;
	long long temp;
	cin >> a >> b;
	while (b != 0)
	{
		temp = a;
		a = b;
		b = temp % b;
	}
	for (long long i = 0; i < a; i++)
		cout << 1;
	cout <<"\n";
	return 0;

}