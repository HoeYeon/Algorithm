#include <iostream>
#include <stack>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	stack<int> s;
	int N;
	cin >> N;
	int sum = 0;
	while (N--)
	{
		int a;
		cin >> a;
		if (a == 0)
			s.pop();
		else
			s.push(a);
	}
	int ss = s.size();
	for (int i = 0; i < ss; i++)
	{
		sum += s.top();
		s.pop();
	}
	cout << sum << "\n";
	return 0;
}