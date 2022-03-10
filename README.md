## Splice Copy

Since Python 3.10 supports the `splice` syscall, this is a new way of copying files. This avoids the transition between user- and kernel space. \
From my findings, it is significantly faster than Python's `shutil.copyfile()`. \
A 3GB `.bin` file took ~1m1s with `copy` from this package, whereas `copyfile()` took ~2m14s. \
Included is a small test script, which generates a bunch of binary files and then tests the MD5 hash from the source and copied file. \
I have locally tested it with `.bin`, `.jpg`, `.txt` and `.pdf` files.