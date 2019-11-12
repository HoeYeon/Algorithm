#include <iostream>
#include <queue>

using namespace std;

//int arr[25][25] = { 0, };
queue<pair<int, int>> q;
int N, M,mmin,result=0;
int a,b;

void dfs(int x, int y, int cnt)
{
	if (x == a && y == b)
	{
		if (cnt == mmin)
			result++;
		return;
	}
	if (x + 1 <= a)
		dfs(x + 1, y, cnt + 1);
	if (y + 1 <= b)
		dfs(x, y + 1, cnt + 1);



}
int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M;
	cin >> a >> b;
	mmin = a + b;
	if (a > N || b > M || (a==0 && b == 0))
		cout << "fail\n";
	else
	{
		dfs(0, 0, 0);
		cout << mmin << "\n" << result << "\n";
	}
	return 0;

}