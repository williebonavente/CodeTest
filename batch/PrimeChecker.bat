@echo off
setlocal

set /p num=Enter a number: 

set isPrime=1

if %num% leq 1 (
    set isPrime=0
) else (
    for /l %%i in (2,1,%num%/2) do (
        if %num% %% %%i equ 0 (
            set isPrime=0
            goto :break
        )
    )
)

:break

if %isPrime% equ 1 (
    echo %num% is a prime number
) else (
    echo %num% is not a prime number
)

endlocal
