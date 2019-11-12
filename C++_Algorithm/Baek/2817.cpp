#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int N, K,count = 0;
		int A[21] = { 0, };
		int check[1001] = { 0, };
		check[0] = 1;
		cin >> N >> K;
		for (int j = 0; j < N; j++)
			cin >> A[j];
		sort(A, A + N);
		for (int j = 0; j <N; j++)
		{
			for (int k = K; k >= 0; k--)
			{
				if (check[k] == 1)
					check[k + A[j]] = 1;
			}
		}
		for (int j = 0; j <N; j++)
		{
			for (int k = K; k >= 0; k--)
			{
				if (check[k] == 1)
				{
					check[k + A[j]] = 1;
					if (k + A[j] == K)
						count++;
				}
			}
		}
		cout << "#" << i << " " << count << endl;

	}
	return 0;
}