$factcount = 0
@fact: $factcount = $factcount + 1
%x = param
if %x <= 1 jump @basecase
%sub1 = %x - 1
param %sub1
%rest = call @fact 1
%result = %rest * %x
return %result
@basecase: return 1
@main: %n = 3
param %n
%res = call @fact 1
return %res