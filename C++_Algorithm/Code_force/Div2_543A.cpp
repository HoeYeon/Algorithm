#include <iostream>
#include <vector>

using namespace std;

struct ss {
	int sc;
	int po;
};
int main()
{
	ss student[101];
	int school[101] = { 0, };
	vector <int> v;
	int n, m, k,count=0;
	cin >> n >> m >> k;

	for (int i = 1; i <= n; i++)
		cin >> student[i].po;
	for (int i = 1; i <= n; i++)
	{
		int a;
		cin >> a;
		student[i].sc = a;
		if (school[a] < student[i].po)
			school[a] = student[i].po;
	}
	for (int i = 0; i < k; i++)
	{
		int a;
		cin >> a;
		v.push_back(a);
	}
	int len = v.size();
	for (int i = 0; i < len; i++)
	{
		if (school[student[v[i]].sc] != student[v[i]].po)
			count++;
	}
	cout << count << "\n";
	return 0;
}