@echo off
setlocal

set /p num=Enter a number: 

set sum=0
for /l %%i in (0,1,%{num}.length%) do (
    set /a sum+=%{num}:~%%i,1
)

echo The sum of digits in %num% is %sum%

endlocal
