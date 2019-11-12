#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;


int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	//cout << fixed;
	//cout.precision(7);
	//int *sum = new int[N];
	//vector<pair<int, int>> met;

	int N;
	cin >> N;
	vector<int> v;
	vector<int> v2;
	int temp;
	double sum = 0;
	int arr[8001] = { 0, };
	int two, three, four;
	double one;
	int max = -4001 , min = 4001;

	for (int i = 0; i < N; i++)
	{
		cin >> temp;
		v.push_back(temp);
		sum += temp;
		if (temp < 0)
			arr[temp + 8001]++;
		else
			arr[temp]++;
		if (temp > max)
			max = temp;
		if (temp < min)
			min = temp;
	}
	int temp2 = 0;
	for (int i = 0; i < 8001; i++)
	{
		if (temp2 < arr[i])
			temp2 = arr[i];
	}

	for (int i = 0; i < 8001; i++)
	{
		if (arr[i] == temp2)
			if (i > 4000)
				v2.push_back((i - 8001));
			else
				v2.push_back(i);
	}
	sort(v.begin(), v.end());
	sort(v2.begin(), v2.end());

	//sum = sum / v.size();
	one = floor(sum / v.size() + 0.5);
	//one = floor(sum + 0.5) / 10;
	two = v[ceil(v.size() / 2)];

	if (v2.size() == 1)
		three = v2[0];
	else
		three = v2[1];
	four = max - min;

	cout << one << "\n" << two << "\n"<< three << "\n" << four << "\n";


	return 0;

}