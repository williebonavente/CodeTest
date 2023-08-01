@echo off
setlocal

set /p radius=Enter the radius of the circle: 

set /a area=3.14159 * %radius% * %radius%

echo The area of the circle with radius %radius% is %area%

endlocal
