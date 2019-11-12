#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;

	long long add_tmp=0, result=0, tmp=0, cc = 0;
	stack <int> s;
	s.push(1);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string str;
		cin >> str;
		if (str == "for")
		{
			int num;
			cin >> num;
			cc++;
			s.push(num);
		}
		else if (str == "add")
		{
			if (cc == 0)
				result++;
			else
				tmp++;
		}
		else if (str == "end")
		{
			if (add_tmp >= 4294967295 || result >= 4294967295)
				break;
			int tt = s.top();
			s.pop();
			add_tmp = tt * (tmp + add_tmp);
			cc--;
			tmp = 0;
			if (cc == 0)
				result += add_tmp;
		}
	}
	if (result >= 4294967295 || add_tmp >= 4294967295)
		cout << "OVERFLOW!!!" << endl;
	else
		cout << result << endl;
	return 0;
}