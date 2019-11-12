#include <iostream>
#include <queue>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int N, K,count=0;
	cin >> N >> K;
	queue<int> q;
	for (int i = 0; i < N; i++)
	{
		int a;
		cin >> a;
		q.push(a);
	}
	while (!q.empty())
	{
		if (K < q.front())
			break;
		count++;
		K -= q.front();
		q.pop();
	}
	cout << count << endl;
	return 0;
}