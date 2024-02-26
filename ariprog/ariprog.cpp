/*
ID: brkwok1
LANG: C++11
TASK: ariprog
*/
#include <iostream>
#include <fstream>

#define MAX_BISQ 125001

using namespace std;

int bisquares[MAX_BISQ];
bool is_bisq[MAX_BISQ];

int main()
{
  ifstream fin("ariprog.in");
  ofstream fout("ariprog.out");

  int N, M, i, j, max_bs, max_seq, count = 0;

  fin >> N >> M;

  for (i = 0; i <= M; i++)
  {
    for (j = i; j <= M; j++)
    {
      int bs = i * i + j * j;
      bisquares[bs] = bs;
      is_bisq[bs] = true;
      max_bs = bs;
    }
  }

  max_bs += 1;

  max_seq = max_bs / (N - 1) + 2;

  for (int b = 1; b <= max_seq; b++)
  {
    for (int a = 0; a < max_bs; a++)
    {
      int x = a;

      for (i = 0; i < N; i++)
      {
        if (x >= max_bs || !is_bisq[x])
        {
          break;
        }

        x += b;
      }

      if (i == N)
      {
        fout << bisquares[a] << " " << b << "\n";
        count += 1;
      }
    }
  }

  if (count == 0)
    fout << "NONE\n";

  return 0;
}