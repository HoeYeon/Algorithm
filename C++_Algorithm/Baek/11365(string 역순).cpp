#include <iostream>
#include <stack>
#include <string>

/*
#include <algorithm>
string s;

getline(cin, s);
if (s == "END")break;
reverse(s.begin(), s.end());
cout << s << "\n";
*/
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	string t;
	stack<char> s;
	while (true)
	{
		getline(cin, t);
		if (t == "END")
			break;
		for (int i = 0; i < t.length(); i++)
			s.push(t[i]);
		for (int i = 0; i < t.length(); i++)
		{
			cout << s.top();
			s.pop();
		}
		cout << "\n";
	}
}