#include <iostream>
#include <vector>
using namespace std;


int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;

	long long N;
	vector<int> a;
	cin >> N;

	while (N != 0)
	{
		a.push_back(N % 10);
		N /= 10;
	}
	
	return 0;

}