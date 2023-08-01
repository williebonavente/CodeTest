@echo off
setlocal

set /p limit=Enter the limit for the Fibonacci sequence: 

set num1=0
set num2=1

echo %num1%
echo %num2%

for /l %%i in (2,1,%limit%) do (
    set /a sum=%num1%+%num2%
    echo !sum!
    set num1=%num2%
    set num2=!sum!
)

endlocal
