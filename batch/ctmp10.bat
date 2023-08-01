@echo off

setlocal enabledelayedexpansion

REM Define the array
set array[0]=5
set array[1]=2
set array[2]=8
set array[3]=1
set array[4]=3

REM Get the length of the array
set length=5

REM Sort the array using bubble sort algorithm
for /L %%i in (0,1,%length%) do (
    for /L %%j in (0,1,%length%) do (
        if !array[%%i]! lss !array[%%j]! (
            set "temp=!array[%%i]!"
            set "array[%%i]=!array[%%j]!"
            set "array[%%j]=!temp!"
        )
    )
)

REM Print the sorted array
for /L %%i in (0,1,%length%) do (
    echo !array[%%i]!
)

endlocal
