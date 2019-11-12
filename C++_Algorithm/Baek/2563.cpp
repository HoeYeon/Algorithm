#include <iostream>

using namespace std;

int main() {
	int arr[101][101] = { 0, };
	int N;
	int count = 0;
	cin >> N;
	while (N--)
	{
		int a, b;
		cin >> a >> b;
		for (int i = a; i < a + 10; i++)
		{
			for (int j = b; j < b + 10; j++)
			{
				if (arr[i][j] == 0)
				{
					arr[i][j] = 1;
					count++;
				}
			}
		}
	}
	cout << count << endl;
	return 0;
}