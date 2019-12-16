#include <iostream>

using namespace std;

int arr[2200][2200] = { 0, };
int go[9][2] = { {0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2} };
int result[3] = { 0, };
void dfs(int n, int x, int y) {
	//cout << "n:" << n << endl;
	if (n == 1) {
		if (arr[x][y] == 1){
			result[2]++;
			//cout << "n==1 && one:" << x << y << endl;
		}
		else if (arr[x][y] == 0){
			result[1]++;
			//cout << "n==1 && zero:" << x << y << endl;
		}
		else {
			result[1]++;
		}
		return;
	}
	for (int i = 0; i < 9; i++) {
		int start = arr[x + go[i][0] * (n / 3)][y + go[i][1] * (n / 3)];
		int check = 1;
		for (int j = x + go[i][0] * (n / 3); j < x + (1 + go[i][0]) * (n / 3); j++) {
			if (check == 0)
				break;
			for (int k = y + go[i][1] * (n / 3); k < y + (1 + go[i][1]) * (n / 3); k++) {
				if (check == 0)
					break;
				if (start != arr[j][k]) {
					dfs(n / 3, x + go[i][0] * (n / 3), y + go[i][1] * (n / 3));
					check = 0;
				}
			}
		}
		if (check == 1) {
			if (start == 0)
				result[1]++;
			else if (start == 1)
				result[2]++;
			else
				result[0]++;
		}
	}

}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			cin >> arr[i][j];
	}
	int tmp = 0;
	for (int i = 1; i < N; i++) {
		for (int j = 1; j < N; j++) {
			if (arr[i][j] != arr[i][j - 1] || arr[i][j] != arr[i - 1][j - 1])
				tmp = 1;
		}
	}
	if (tmp == 0) {
		result[arr[0][0] + 1]++;
		cout << result[0] << "\n" << result[1] << "\n" << result[2] << "\n";
		return 0;
	}
	dfs(N, 0, 0);
	cout << result[0] << "\n" << result[1] << "\n" << result[2] << "\n";
	return 0;
}