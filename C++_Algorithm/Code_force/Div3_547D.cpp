#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int check1[150000] = { 0, };
int check2[150000] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n,count=0;
	string s1, s2;
	vector <int> v1[27];
	vector <int> v2[27];
	vector <pair<int, int>> result;
	//v.push_back('a'-97); == 0
	cin >> n;
	cin >> s1 >> s2;
	for (int i = 0; i < n; i++)
	{
		int a = s1[i] - 97;
		int b = s2[i] - 97;
		if (s1[i] == '?')
			v1[26].push_back(i + 1);
		else
			v1[a].push_back(i + 1);
		if (s2[i] == '?')
			v2[26].push_back(i + 1);
		else
			v2[b].push_back(i + 1);
	}
	
	for (int i = 0; i < 26; i++)
	{
		if (v1[i].size() > 0 && v2[i].size() > 0)
		{
			int size = min(v1[i].size(), v2[i].size());
			for (int j = 0; j < size; j++)
			{
				result.push_back(make_pair(v1[i][j], v2[i][j]));
				check1[v1[i][j]] = 1;
				check2[v2[i][j]] = 1;
				count++;
			}
		}
	}
	int l1 = v1[26].size()-1, l2 = v2[26].size()-1;
	for (int i = 0; i < 27; i++)
	{
		int size = v1[i].size();
		for (int j = 0; j < size; j++)
		{
			if (check1[v1[i][j]] == 1 || l2 < 0)
				continue;
			result.push_back(make_pair(v1[i][j], v2[26][l2]));
			check1[v1[i][j]] = 1;
			check2[v2[26][l2]] = 1;
			l2--;
			count++;
		}
		size = v2[i].size();
		for (int j = 0; j < size; j++)
		{
			if (check2[v2[i][j]] == 1 || l1<0)
				continue;
			result.push_back(make_pair(v1[26][l1], v2[i][j]));
			check1[v1[26][l1]] = 1;
			check2[v2[i][j]] = 1;
			l1--;
			count++;
		}
	}
	cout << count << "\n";
	for (int i = 0; i < result.size(); i++)
		cout <<result[i].first << "  " << result[i].second << "\n";
	return 0;
}