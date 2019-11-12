#include <iostream>
#include <algorithm>

using namespace std;
struct Point {
	int x;
	int y;
};
bool cmp(const Point &p1, const Point &p2) {
	if (p1.x < p2.x) {
		return true;
	}
	else if (p1.x == p2.x) {
		return p1.y < p2.y;
	}
	else {
		return false;

	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int N;
	cin >> N;
	Point a[100000];
	for (int i = 0; i < N; i++)
		cin >> a[i].x >> a[i].y;
	
	sort(a, a + N, cmp);
	for (int i = 0; i < N; i++)
		cout << a[i].x << " " << a[i].y << "\n";
	return 0;
}