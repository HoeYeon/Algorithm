#include <iostream>
#include <queue>

using namespace std;


int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;
	int i = 1;
	while (true)
	{
		if (i % 2 == 1 && i % 3 == 0 && i % 5 == 4)
			break;
		i++;
	}
	cout << i;
	return 0;

}