#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	string s;
	cin >> s;
	int i = 1;
	cout << s[0];
	while (s[i] != NULL)
	{
		if (s[i] == '-')
			cout << s[i + 1];
		i++;
	}
	cout << "\n";
	
	return 0;
}