#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> findpair(int n, int a0, int step, long long p)
{
	map<int, int> m;
	for (int i = 0; i < n; i++)
	{
		m[a0] = i;
		if (a0 == 0)
		{
			if (p == 0)
				return{ i,i };
		}
		else if (p%a0 == 0)
		{
			map<int, int>::iterator iter = m.find(p / a0);
			if (iter != m.end())
				return{ i,iter->second };
			
		}
		a0 += step;
	}
	return {};
}
int main(void) {

	

	return 0;

}