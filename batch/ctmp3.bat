@echo off
setlocal

set /p num=Enter a number: 

set fact=1
for /l %%i in (1,1,%num%) do (
    set /a fact*=%%i
)

echo The factorial of %num% is %fact%

endlocal
