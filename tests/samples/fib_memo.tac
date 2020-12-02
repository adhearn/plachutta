main: n = 10
fibs = memrequest n
i = 0
fib: if i >= n jump fibend
if i == 0 jump if0
if i == 1 jump if1
tmp1 = i - 1
tmp2 = i - 2
prev1 = fibs[tmp1]
prev2 = fibs[tmp2]
fibs[i] = prev1 + prev2
jump ifend
if0: fibs[i] = 0
jump ifend
if1: fibs[i] = 1
ifend: i = i + 1
jump fib
fibend: lastindex = n - 1
result = fibs[lastindex]
return result
