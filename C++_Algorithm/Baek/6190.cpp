#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N,last = -1;
		int count = 1, a = 0, b = 0,result=-1;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			int temp;
			cin >> temp;
			while (temp != 0)
			{
				if (last > temp % 10)
				{
					if(count > 2)
						result = max(result, a*b);
					count = 1;
					a = 0;
					b = 0;
				}
				if (count % 2 == 1)
				{
					a = temp % 10;
					last = a;
				}
				else
				{
					b = temp % 10;
					last = b;
				}
				if (count >= 2)
					result = max(result, a*b);
				cout << result << " ";
				temp /= 10;
				count++;
			}
		}
		cout << "#" << i;
		cout << " " << result << "\n";
	}
	return 0;
}