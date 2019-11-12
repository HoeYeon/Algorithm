#include <iostream>
#include <queue>

using namespace std;


int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;
	queue<int> f;
	queue<int> s;

	int N, M;

	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		f.push(i + 1);
	}
	while (!f.empty())
	{
		int count = 1;
		while (count%M != 0)
		{
			int temp = f.front();
			f.pop();
			f.push(temp);
			count++;
		}
		s.push(f.front());
		f.pop();
	}
	cout << "<";
	for (int i = 0; i < N; i++)
	{
		cout << s.front();
		if (i != N - 1)
			cout << ", ";
		s.pop();
	}
	cout << ">" << endl;

	return 0;

}