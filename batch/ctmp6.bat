@echo off
setlocal

set /p celsius=Enter the temperature in Celsius: 

set /a fahrenheit=(%celsius% * 9 / 5) + 32

echo %celsius% degrees Celsius is equal to %fahrenheit% degrees Fahrenheit

endlocal
