def solve(s):
    slist = s.split( )
    cap = []
    cap.append(slist[0].capitalize())
    cap.append(slist[1].capitalize())
    ans = " ".join(cap)
    print (ans)

s = input()
solve(s)


