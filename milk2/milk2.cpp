/*
ID: brkwok1
LANG: C++11
TASK: milk2
*/
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

bool cmp(int a1[], int a2[])
{
  return a1[0] < a2[0];
}

int main()
{
  ifstream fin("milk2.in");
  ofstream fout("milk2.out");

  int N, s, e, i;
  vector<vector<int>> interval;

  fin >> N;

  for (i = 0; i < N; ++i)
  {
    fin >> s >> e;
    vector<int> v = {s,e};
    interval.push_back(v);
  }

  sort(interval.begin(), interval.end(), cmp);

  for (i = 0; i < interval.size(); i++)
  {
    for (int j = 0; j < 2; j++)
    {
      cout << interval[i][j] << endl;
    }
  }

  return 0;
}