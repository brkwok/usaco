/*
ID: brkwok1
LANG: C++11
TASK: ride
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
  ifstream fin("ride.in");
  ofstream fout("ride.out");
  
  string x, y;
  fin >> x >> y;

  int c1, c2;
  c1 = c2 = 1;

  for (string::iterator it = x.begin(); it != x.end(); ++it)
  { 
    c1 *= int(*it) - int('A') + 1;
  }

  for (string::iterator it = y.begin(); it != y.end(); ++it)
  {
    c2 *= int(*it) - int('A') + 1;
  }

  if (c1 % 47 == c2 % 47)
  {
    fout << "GO" << "\n";
  } else
  {
    fout << "STAY" << "\n";
  }

  return 0;
}