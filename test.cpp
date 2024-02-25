/*
ID: brkwok1
LANG: C++11
TASK: test
*/
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main()
{
  ifstream fin("test.in");
  ofstream fout("test.out");

  int x,y;

  fin >> x >> y;
  fout << x + y << endl;
  return 0;
}