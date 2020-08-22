return_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))
rday, rmonth, ryear = return_date
dday, dmonth, dyear = due_date

if ryear > dyear:
    print(10000)
elif ryear == dyear:
    if rmonth > dmonth:
        print(500 * (rmonth - dmonth))
    elif rmonth == dmonth:
        if rday > dday:
            print(15 * (rday - dday))
    else:
        print(0)
else:
    print(0)
