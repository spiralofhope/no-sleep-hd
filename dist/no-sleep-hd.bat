@ECHO OFF



NET FILE 1>NUL 2>NUL & IF ERRORLEVEL 1 (
  ECHO Right-click and run this as administrator.
  PAUSE
  EXIT /B
)


CD /D "%~dp0"
no-sleep-hd.exe
