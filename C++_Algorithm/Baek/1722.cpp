#include <iostream>
#include <vector>

using namespace std;

vector<int> arr;
int ans[21];

long long fac(long long a)
{
	long long result = 1;
	for (int i = 2; i <= a; i++)
		result *= i;
	return result;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int N, check;
	long long k;
	for (int i = 0; i < 21; i++)
		arr.push_back(i);
	cin >> N >> check;
	if (check == 1)
	{
		cin >> k;
		for (int i = 1; i <= N; i++)
		{
			long long temp = fac(N - i);
			int j = 1;
			while (k > temp)
			{
				k -= temp;
				j++;
			}
			ans[i] = arr[j];
			arr.erase(arr.begin()+j);
		}
		for (int i = 1; i <= N; i++)
			cout << ans[i] << " ";
		cout << endl;
	}
	else
	{
		long long answer = 1;
		for (int i = 1; i <= N; i++)
			cin >> ans[i];
		for (int i = 1; i <= N; i++)
		{
			int j = 1;
			long long temp = fac(N - i);
			while (ans[i] != arr[j])
			{
				answer += temp;
				j++;
			}
			arr.erase(arr.begin() + j);
		}
		cout << answer << endl;
	}
	return 0;
}