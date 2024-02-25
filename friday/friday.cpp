/*
ID: brkwok1
LANG: C++11
TASK: friday
*/
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <cassert>

#define NUMDAYS 7

using namespace std;

int days[NUMDAYS] = {0};
int d_in_m[] = {31,28,31,30,31,30,31,31,30,31,30,31};
int curr = 2;

bool is_leap(int y)
{
  if ((y % 100 == 0 && y % 400 == 0) || (y % 4 == 0 && y % 100 != 0))
  {
    return true;
  }

  return false;
}

void f_thirteenth(int y)
{
  if (is_leap(y))
    d_in_m[1] = 29;
  else
    d_in_m[1] = 28;

  for (int i = 0 ; i < 12; i++)
  {
    int thirteenth = (curr + 12) % 7;
    days[thirteenth] += 1;
    curr = (curr + d_in_m[i]) % 7;
  }
}

int N, start_y, end_y;

int main()
{
  ifstream fin("friday.in");
  ofstream fout("friday.out");

  fin >> N;
  start_y = 1900;
  end_y = 1900 + N;

  for (int i = start_y; i < end_y; i++)
  {
    f_thirteenth(i);
  }

  for (int i = 0; i < 7; i++)
  {
    fout << days[i] << " ";
  }
  fout << endl;

  return 0;
}