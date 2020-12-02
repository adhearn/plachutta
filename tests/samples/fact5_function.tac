fact: x = param 0
if x <= 0 jump basecase
sub1 = x - 1
param sub1
rest = call fact 1
result = x * rest
return result
basecase: return 1
main: param 5
result = call fact 1
return result
