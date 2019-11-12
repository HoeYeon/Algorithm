#include <iostream>
#include <algorithm>

using namespace std;

int arr[401] = { 0, };
int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		for (int i = 1; i <= 400; i++)
			arr[i] = 0;
		int N;
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			int a, b;
			cin >> a >> b;
			if (a > b)
				swap(a, b);
			if (a % 2 == 1)
				a++;
			if (b % 2 == 1)
				b++;
			for (a; a <= b; a++)
				arr[a]++;
		}
		int maxx = 0;
		for (int i = 1; i <= 400; i++)
			maxx = max(maxx, arr[i]);
		cout << "#" << tc << " " << maxx << "\n";
	}
	return 0;

}