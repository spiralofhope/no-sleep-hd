# About

Keep a hard drive from going to sleep.

This uses the brute-force method of periodically reading random sectors.

To change the drive letter and timing, manually edit the source code.



# Configuration

Edit `no-sleep-hd.py` and customize the two variables:

```python
EXT_DRIVE_NAME = "B"
PERIOD_SECS = 90
```



# Setup / Compilation

Tested 2025-03-17 with Python 3.7.4 on Windows 11:

- You may have to install [Python](https://www.python.org/).
  - The necessary program [Pip](https://www.pypa.io/) should already be installed alongside Python.
- `double-click` the file `create-py2exe.bat`



# "Installation"

A new `dist` directory was created from the setup.  All the files within are necessary.  You can rename this directory and move it elsewhere if you wish.



# Execution

- Go to the new `dist` directory.
- `double-click` the file `no-sleep-hd.bat`.



# "Uninstallation"

- Exit the program with `control-c` or close its window.
- Then delete the files or directory.

If you just want to restore the files back to the pre-compilation state, you can run the `cleanup.bat` file in the `dist` directory.
