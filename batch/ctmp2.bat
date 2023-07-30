@echo off
setlocal enabledelayedexpansion

rem a) the set of people who speak English, the set of people who speak English with an Australian accent
set "englishPeople=John Mary Alice Bob"
set "australianAccentPeople=John Alice"

call :IsSubset "%englishPeople%" "%australianAccentPeople%"
goto :next

rem b) the set of fruits, the set of citrus fruits
set "fruits=apple banana orange pear"
set "citrusFruits=orange lemon lime"

call :IsSubset "%fruits%" "%citrusFruits%"
goto :next

rem c) the set of students studying discrete mathematics, the set of students studying data structures
set "discreteMathStudents=John Alice Bob"
set "dataStructuresStudents=John Mary"

call :IsSubset "%discreteMathStudents%" "%dataStructuresStudents%"

:next
pause
exit /b

:IsSubset
set "isSubset=true"
for %%x in (%1) do (
    echo "%2" | find /i "%%x" > nul
    if errorlevel 1 (
        set "isSubset=false"
        goto :break
    )
)
:break
if "%isSubset%"=="true" (
    echo The first set is a subset of the second.
) else if "%isSubset%"=="false" (
    for %%x in (%2) do (
        echo "%1" | find /i "%%x" > nul
        if errorlevel 1 (
            set "isSubset=false"
            goto :notASubset
        )
    )
    :notASubset
    if "%isSubset%"=="false" (
        echo Neither set is a subset of the other.
    ) else (
        echo The second set is a subset of the first.
    )
)
exit /b
