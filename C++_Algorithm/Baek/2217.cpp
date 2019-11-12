#include <iostream>
#include <algorithm>
using namespace std;

int arr[100000];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int tmp;
		cin >> tmp;
		arr[i] = -tmp;
	}
	sort(arr, arr + N);
	int max = -arr[0];
	for (int i = 1; i< N;i++)
	{
		if (-arr[i]*(i+1) > max)
			max = -arr[i] * (i + 1);
	}
	cout << max << endl;
	return 0;
}