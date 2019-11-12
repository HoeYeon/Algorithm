#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); //cin 실행속도 향상
	int N, K;

	while (1)
	{
		cin >> N >> K;
		if (N == 0 && K == 0)
			break;

		long long result = 1;
		if (N - K < K)
			K = N - K;
	
		for (int i = 1; i <= K; i++)
		{
			result *= N;
			result /= i;
			N--;
		}
		cout << result << "\n";
	}
	return 0;

}

