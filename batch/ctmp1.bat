@echo off
setlocal enabledelayedexpansion

rem a) {x | x is a real number such that x^2 = 1}
echo The members of the set are: 1, -1

rem b) {x | x is a positive integer less than 12}
echo The members of the set are:
for /l %%i in (1, 1, 11) do (
    echo %%i
)

rem c) {x | x is the square of an integer and x < 100}
echo The members of the set are:
for /l %%i in (1, 1, 10) do (
    set /a square=%%i * %%i
    if !square! lss 100 (
        echo !square!
    )
)

rem d) {x | x is an integer such that x^2 = 2}
echo The members of the set are: -1, 1
