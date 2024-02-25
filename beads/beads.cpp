/*
ID: brkwok1
LANG: C++11
TASK: beads
*/
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <cassert>

using namespace std;

int main()
{
  ifstream fin("beads.in");
  ofstream fout("beads.out");
  int N, max = 0, streak, state, i, j;
  string s;
  char c;

  fin >> N >> s;
  s = s + s;

  for (i = 0; i < N; i++)
  {
    c = (char)s[i];

    if (c == 'w')
    {
      state = 0;
    }
    else
    {
      state = 1;
    }

    j = i;
    streak = 0;
    while (state <= 2)
    {
      while (j < N + i && (s[j] == c || s[j] == 'w'))
      {
        j++;
        streak++;
      }
      state++;
      c = s[j];
    }
    if (streak > max)
    {
      max = streak;
    }
  }

  fout << max << endl;

  return 0;
}