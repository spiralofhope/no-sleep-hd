Keep a hard drive from going to sleep.

This uses the brute-force method of periodically reading random sectors.

To change the drive letter and timing, manually edit the source code.

Tested 2025-03-17 with Python 3.9.2 on Windows 11 with Windows Subsystem for Linux (Debian):

```bash
python no-sleep-hd.py
```

Tested 2025-03-17 with Python 3.11.9 on Windows 11

```bat
pip install py2exe
create-py2exe.bat

dist/no-sleep-hd.exe
```
