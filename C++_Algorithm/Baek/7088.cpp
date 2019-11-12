#include <iostream>

using namespace std;

int cow[100001][4] = { 0, };
int main(void) {
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++)
	{
		
		int N, Q, L, R;
		cin >> N >> Q;
		for (int j = 1; j <= N; j++)
		{
			int a;
			cin >> a;
			cow[j][1] = cow[j - 1][1];
			cow[j][2] = cow[j - 1][2];
			cow[j][3] = cow[j - 1][3];
			cow[j][a]++;
		}
		
		for (int j = 0; j < Q; j++)
		{
			cin >> L >> R;
			for (int k = 1; k < 4; k++)
				cout << cow[R][k] - cow[L-1][k] << " ";
			cout << "\n";
		}
	}
	return 0;

}
