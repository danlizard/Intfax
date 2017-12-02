from getnews import *
from getkeywords import *

def getTwits(header):
    v = TSearch(make_header(header)).get()
    ans = ["Z", 0, 0, 0]
    for el in v:
        ans[0] = min(ans[0], v[el][0])
        ans[1] += v[el][1]
        ans[2] += v[el][2]
        ans[3] += v[el][3]
    return ans

if __name__ == "__main__":
    z = getTwits(input())
    print(len(z))
    print(z)