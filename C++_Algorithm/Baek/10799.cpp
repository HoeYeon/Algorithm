#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	string ss;
	stack<int> s;
	cin >> ss;
	int count = 0;
	for (int i = 0; i < ss.size(); i++)
	{
		if (ss[i] == '(')
			s.push(1);
		else
		{
			if (ss[i - 1] == ')')
			{
				count++;
				s.pop();
			}
			else
			{
				s.pop();
				count += s.size();
			}
		}
	}
	cout << count << "\n";

	return 0;
}