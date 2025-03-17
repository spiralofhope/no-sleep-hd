@ECHO OFF

REM Clean up files that might have been created by create-py2exe.bat or create-py2exe.sh



CD /D "%~dp0"

del /F /Q "_bz2.pyd"
del /F /Q "_ctypes.pyd"
del /F /Q "_hashlib.pyd"
del /F /Q "libcrypto-1_1.dll"
del /F /Q "library.zip"
del /F /Q "libssl-1_1.dll"
del /F /Q "_lzma.pyd"
del /F /Q "no-sleep-hd.exe"
del /F /Q "pyexpat.pyd"
del /F /Q "python37.dll"
del /F /Q "select.pyd"
del /F /Q "_socket.pyd"
del /F /Q "_ssl.pyd"
del /F /Q "unicodedata.pyd"
