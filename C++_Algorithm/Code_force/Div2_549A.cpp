#include <iostream>

using namespace std;

int arr[200001] = { 0, };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	int zero=0, one=0,count = 0;
	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		if (a == 0)
			zero++;
		else
			one++;
		arr[i] = a;
	}
	int temp = 0;
	while (zero != 0 && one != 0)
	{
		if(arr[temp] == 0)
			zero--;
		else
			one--;
		temp++;
		count++;
	}
	cout << count << "\n";
	return 0;
}