/*
ID: brkwok1
LANG: C++11
TASK: gift1
*/
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <cassert>

using namespace std;

#define MAXPEOPLE 10
#define NAMELEN 32

struct Person
{
  string name;
  int total;
};

Person people[MAXPEOPLE];
int N;

Person *find(string name)
{
  for (int i = 0; i < N; i++)
  {
    if (people[i].name == name)
      return &people[i];
  }

  assert(0);
}

int main()
{
  ifstream fin("gift1.in");
  ofstream fout("gift1.out");

  fin >> N;
  int i, withdrawl, dist;
  string name, to;

  for (i = 0; i < N; i++)
  {
    Person p;
    fin >> p.name;
    p.total = 0;

    people[i] = p;
  }

  for (i = 0; i < N; i++)
  {
    fin >> name >> withdrawl >> dist;
    Person *p1, *p2;
    p1 = find(name);

    if (dist > 0)
    {
      p1->total -= withdrawl - (withdrawl % dist);
    }

    for (int j = 0; j < dist; j++)
    {
      fin >> to;
      p2 = find(to);
      p2->total += withdrawl / dist;
    }
  }

  for (i = 0; i < N; i++)
  {
    Person p = people[i];
    fout << p.name << " " << p.total << endl;
  }
}