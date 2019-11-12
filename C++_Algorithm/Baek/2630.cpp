#include <iostream>

using namespace std;

int arr[150][150] = { 0, };
int go[4][4] = { {0,0},{0,1},{1,0},{1,1} };
int white = 0, blue = 0;
void dfs(int n,int x, int y) {
	if (n == 1) {
		if (arr[x][y] == 1)
			blue++; 
		else
			white++;
		return;
	}
	for (int i = 0; i < 4; i++){
		int x_ = x + go[i][0] * (n / 2);
		int y_ = y + go[i][1] * (n / 2);
		int start = arr[x_][y_];
		int check = 1;
		for (int j = x_; j < x + (1 + go[i][0]) * (n / 2); j++){
			if (check == 0)
				break;
			for (int k = y_; k < y + (1 + go[i][1]) * (n / 2); k++) {
				if (check == 0)
					break;
				if (start != arr[j][k]) {
					dfs(n / 2, x_, y_);
					check = 0;
				}
			}
		}
		if (check == 1) {
			if (start == 0)
				white++;
			else
				blue++;
		}
	}
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)	{
		for (int j = 0; j < N; j++)
			cin >> arr[i][j];
	}
	dfs(N, 0, 0);
	cout << white << endl << blue << endl;

	return 0;
}