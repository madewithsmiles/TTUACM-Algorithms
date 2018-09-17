/*
def kangaroo(x1, v1, x2, v2):
    velDiff = v2 - v1
    posDiff = x1 - x2
    # If you divide by 0 then j is undefined
    if velDiff != 0:
        # If j is a positive integer (no negative or partial jumps)
        if posDiff % velDiff == 0 and posDiff / velDiff > 0:
            return 'YES'
    # Otherwise there is no j that satisfies our conditions
    return 'NO'
*/

#include <iostream>
#include <string>

string kangaroo(int x1, int v1, int x2, int v2)
{
  int velDiff = v2 - v1;
  int posDiff = x1 - x2;
  
  if (velDiff != 0)
  {
    if (posDiff % velDiff == 0 && posDiff / velDiff > 0)
    {
      return "YES";
    }
  }
  return "NO";
}
