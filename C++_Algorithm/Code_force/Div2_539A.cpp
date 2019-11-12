#include <iostream>
#include<algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n, v,cost=0;
	cin >> n >> v;
	if (n > v)
		cost += v;
	else
		cost += n - 1;
	int i = 2;
	while (n > v + 1)
	{
		cost += i;
		v += 1;
		i++;
	}
	cout << cost << "\n";
	return 0;
}