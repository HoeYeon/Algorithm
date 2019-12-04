#include <iostream>

using namespace std;

int arr[15][15];
int result = 0;
int N;
bool check(int x, int y) {
	for (int i = 0; i < x; i++) {
		if (arr[i][y] == 1)
			return false;
	}
	int xx = x;
	int yy = y;
	while (xx >= 0 && yy >= 0) {
		if (arr[xx][yy] == 1)
			return false;
		xx--;
		yy--;
	}

	xx = x;
	yy = y;
	while (xx >= 0 && yy < N) {
		if (arr[xx][yy] == 1)
			return false;
		xx--;
		yy++;
	}
	return true;
}

void dfs(int x) {
	if (x == N) {
		result++;
		return;
	}
	for (int i = 0; i < N; i++) {
		if (check(x, i)) {
			arr[x][i] = 1;
			dfs(x + 1);
			arr[x][i] = 0;
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	dfs(0);
	cout << result << "\n";


	return 0;
}