#include <iostream>
#include <vector>

using namespace std;

int arr[100001] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		int a, b;
		cin >> a >> b;
		if (a == -1)
			arr[i] = 1;
		else
		{
			if (b == 0)
			{
				arr[a] = 1;
				arr[i] = 1;
			}
		}
	}
	int count = 0;
	vector <int> v;
	for (int i = 1; i <= n; i++)
	{
		if (arr[i] == 0)
		{
			v.push_back(i);
			count++;
		}
	}
	if (count == 0)
		cout << -1 << "\n";
	else
	{
		for (int i = 0; i < v.size(); i++)
			cout << v[i] << " ";
		cout << "\n";
	}
	return 0;
}