@echo off
setlocal

set arr=5 2 8 1 9

for /l %%i in (0,1,%{arr}.length%) do (
    for /l %%j in (0,1,%{arr}.length%-2) do (
        set /a idx=%%j+1
        if !{arr}[%%j]! gtr !{arr}[!idx!]! (
            set temp=!{arr}[%%j]!
            set {arr}[%%j]=!{arr}[!idx!]!
            set {arr}[!idx!]=!temp!
        )
    )
)

echo Sorted array: %arr%

endlocal
