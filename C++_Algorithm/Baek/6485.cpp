#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int root[5001] = { 0, };
		int A,B,C,N,P;
		vector<int> v;
		cin >> N;
		
		for (int j = 0; j < N; j++)
		{
			cin >> A >> B;
			for (int k = A; k <= B; k++)
				root[k]++;
		}
		cin >> P;
		for (int j = 0; j < P; j++)
		{
			cin >> C;
			v.push_back(root[C]);
		}
		cout << "#" << i << " ";
		for (int j = 0; j < v.size(); j++)
			cout  << v[j] << " ";
		cout << "\n";
	}
	return 0;
}