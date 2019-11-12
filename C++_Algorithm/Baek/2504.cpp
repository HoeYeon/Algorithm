#include <iostream>
#include <stack>
#include <string>

using namespace std;

struct brack {
	char c;
	int count;
};

int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;

	stack<brack> s;
	stack<int> re;
	string T;

	cin >> T;
	int i = 0;
	int result=0;
	int c = 0;

	while (T[i] != NULL)
	{
		if (T[i] == '(' || T[i] == '[')
		{
			if (i > 0 && (T[i - 1] == ')' || T[i - 1] == ']'))
			{
				brack temp;
				temp.c = '+';
				temp.count = result;
				s.push(temp);
				result = 0;
			}
			brack b;
			b.c = T[i];
			c++;
			b.count = c;
			s.push(b);
		}
		else
		{
			if (s.empty())
			{	result = 0; break;}
			brack temp = s.top();
			s.pop();
			if (T[i] == ')' && temp.c == '(')
				if (c == temp.count)
					result += 2;
				else
					result *= 2;
			else if (T[i] == ']' && temp.c == '[')
				if (c == temp.count)
					result += 3;
				else
					result *= 3;
			else
			{
				result = 0;
				break;
			}
		}
		i++;
		while (!s.empty())
		{
			if (s.top().c != '+')
				break;
			brack temp = s.top();
			s.pop();
			result += temp.count;
		}
	}

	if (!s.empty())
		cout << 0 << endl;
	else
		cout << result << endl;


	return 0;

}