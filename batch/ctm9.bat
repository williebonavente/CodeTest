@echo off

rem Set the length of the random string.
set _RNDLength=10

rem Set the characters that can be used in the random string.
set _Alphanumeric=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789

rem Generate a random string.
set _RndAlphaNum=""
for /l %%i in (1,1,%_RNDLength%) do (
  set _Rnd=%RANDOM%
  set _RndAlphaNum=!_RndAlphaNum!!_Alphanumeric:~%_Rnd%,1!
)

rem Echo the random string.
echo %_RndAlphaNum%
