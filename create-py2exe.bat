@ECHO OFF



CD /D "%~dp0"



CALL pip install py2exe
:: If necessary, this would work:
:: CALL python -m pip install py2exe
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to install py2exe.
    PAUSE
    EXIT /B
)


ECHO.
ECHO.
ECHO py2exe installation was successful.
ECHO.
ECHO.


CALL python setup.py py2exe
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to run python setup.py py2exe.
    PAUSE
    EXIT /B
)


ECHO.
ECHO.
ECHO Python setup was successful.
ECHO.
ECHO.


ECHO.
ECHO.
ECHO.
ECHO Compilation successful!
ECHO.
ECHO A new "dist" directory has been created.  Run "no-sleep-hd.bat"


PAUSE
