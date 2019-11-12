#include <iostream>
#include <string>
#include <map>

using namespace std;
/*
if (m.find("f") == m.end()) {
	// not found
}
*/
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T, N;
	string n1, n2;
	cin >> T;
	while (T--)
	{
		cin >> N;
		while (N--)
		{
			int net[100000];
			int count = 0;
			map<string, int> m;
			for (int i = 0; i < 100000; i++)
				net[i] = i;
			cin >> n1 >> n2;
			if (m.find(n1) == m.end())
				m[n1] = count++;
			if (m.find(n2) == m.end())
				m[n2] = count++;


		}
	}
	return 0;
}