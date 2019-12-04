#include <iostream>
#include <algorithm>

using namespace std;

int cow[500001];
int horse[500001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T, N, M;
	int c1, c2;
	cin >> T;
	for (int _ = 0; _ < T; _++) {
		long long min_num = 1e9;
		cin >> N >> M;
		cin >> c1 >> c2;
		for (int i = 0; i < N; i++)
			cin >> cow[i];
		for (int i = 0; i < M; i++)
			cin >> horse[i];
		sort(cow, cow + N);
		sort(horse, horse + M);
		int count = 1;
		int i1 = 0, i2 = 0;
		while (1) {
			int dist = abs(c1 - c2) + abs(cow[i1] - horse[i2]);
			if (dist < min_num) {
				count = 1;
				min_num = dist;
			}
			else if (dist == min_num)
				count++;
			if (i1 == N - 1 && i2 == M - 1)
				break;
			if (i1 == N - 1)
				i2++;
			else if (cow[i1] < horse[i2] || i2 == M - 1)
				i1++;
			else
				i2++;
		}
		cout << "Case #" << _+1 << " "<< min_num << " " << count << endl;
	}
	return 0;
}