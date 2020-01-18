#include <iostream>
#include <vector>

using namespace std;

int arr[9][9];
vector<pair<int,int>> v;

bool isOk(int x, int y, int val) {
	for (int i = 0; i < 9; i++) {
		if (arr[i][y] == val || arr[x][i] == val)
			return false;
	}
	int x_ = x / 3 * 3;
	int y_ = y / 3 * 3;

	for (int i = x_; i < x_ + 3; i++) {
		for (int j = y_; j < y_ + 3; j++) {
			if (arr[i][j] == val)
				return false;
		}
	}
	return true;
}
void dfs(int i) {
	if (i == v.size()) {
		for (int p = 0; p < 9; p++) {
			for (int q = 0; q < 9; q++)
				cout << arr[p][q] << " ";
			cout << endl;
		}
		exit(0);
	}
	for (int p = 1; p < 10; p++) {
		if (isOk(v[i].first, v[i].second,p)) {
			arr[v[i].first][v[i].second] = p;
			dfs(i + 1);
			arr[v[i].first][v[i].second] = 0;

		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == 0)
				v.push_back({ i, j });
		}
		
	}
	dfs(0);
	return 0;
}