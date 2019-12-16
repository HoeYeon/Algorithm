#include <iostream>
#include <string>

using namespace std;

char arr[150][150] = { 0, };
int go[4][4] = { {0,0},{0,1},{1,0},{1,1} };
string result = "";
void dfs(int n, int x, int y,int idx) {
	if (n == 1) {
		if (idx == 0)
			result += "(";
		if (arr[x][y] == '1')
			result += "1";
		else
			result += "0";
		if (idx == 3)
			result += ")";
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (i == 0)
			result += "(";
		int x_ = x + go[i][0] * (n / 2);
		int y_ = y + go[i][1] * (n / 2);
		int start = arr[x_][y_];
		int check = 1;
		for (int j = x_; j < x + (1 + go[i][0]) * (n / 2); j++) {
			if (check == 0)
				break;
			for (int k = y_; k < y + (1 + go[i][1]) * (n / 2); k++) {
				if (check == 0)
					break;
				// 영역안에서 다른게 보이면 재귀 실행
				if (start != arr[j][k]) {
					dfs(n / 2, x_, y_,i);
					check = 0;
				}
			}
		}

		if (check == 1) {
			if (start == '0')
				result += "0";
			else
				result += "1";
		}
		if (i == 3)
			result += ")";
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N;
	cin >> N;
	string s;
	for (int i = 0; i < N; i++) {
		cin >> s;
		for (int k = 0; k < N; k++)
			arr[i][k] = s[k];
	}
	int tmp = 0;
	for (int i = 1; i < N; i++)	{
		for (int j = 1; j < N; j++){
			if (arr[i][j] != arr[i][j - 1] || arr[i][j] != arr[i-1][j-1])
				tmp = 1;
		}
	}
	if (tmp == 0) {
		cout << arr[0][0] << endl;
		return 0;
	}
	dfs(N, 0, 0,0);
	cout << result << endl;
	return 0;
}