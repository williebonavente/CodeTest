@echo off
setlocal

set /p str=Enter a string: 

set rev=
for /l %%i in (0,1,%{str}.length%) do (
    set rev=%{str}:~%%i,1%%rev%
)

if "%str%"=="%rev%" (
    echo %str% is a palindrome
) else (
    echo %str% is not a palindrome
)

endlocal
