#!/usr/bin/env  sh

# Clean up any files which might have been created by `create-py2exe.bat` or `create-py2exe.sh`



for file in  \
  _bz2.pyd  \
  _ctypes.pyd  \
  _hashlib.pyd  \
  libcrypto-1_1.dll  \
  library.zip  \
  libssl-1_1.dll  \
  _lzma.pyd  \
  no-sleep-hd.exe  \
  pyexpat.pyd  \
  python37.dll  \
  select.pyd  \
  _socket.pyd  \
  _ssl.pyd  \
  unicodedata.pyd
do
  \rm  --force  --verbose  "$file"
done
