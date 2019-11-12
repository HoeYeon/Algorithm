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

	int T, H, W, N,room;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> H >> W >> N;
		int count = 0;
		for (int j = 1; j <= W; j++)
		{
			for (int k = 1; k <= H; k++)
			{
				count++;
				if (count == N)
					room = k * 100 + j;
			}
		}
		cout << room << endl;
	}
	return 0;

}