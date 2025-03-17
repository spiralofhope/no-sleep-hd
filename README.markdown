Keep a hard drive from going to sleep.

This uses the brute-force method of periodically reading random sectors.

To change the drive letter and timing, manually edit the source code.

Run with

```bash
python no-sleep-hd.py
```

Tested 2025-03-17 with Python 3.9.2 on Windows 11 with Windows Subsystem for Linux.

I have not tested these:

- `create-py2exe.bat`
- `setup.py`

