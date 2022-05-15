import os
import sys

class IsDirectoryError(Exception):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"{self.filename} is a directory.")

class InvalidPlatformError(Exception):
    def __init__(self):
        super().__init__(f"Invalid Platform. Requires Linux with Python >= 3.10.")

# `os.splice()` is only available on Linux and Python >=3.10
_HAS_OS_SPLICE = hasattr(os, "splice") and sys.platform.startswith("linux")

def copy(src: str, dst: str) -> str:
    """Copy data from one fd to another using the splice(2)
    syscall.
    This requires the Linux kernel to be of version >= 2.6.17 and
    glibc to be of version >= 2.5.
    """
    if not _HAS_OS_SPLICE:
        raise InvalidPlatformError()

    if os.path.isdir(src):
        raise IsDirectoryError(src)

    if not os.path.isabs(dst):
        dst = os.path.abspath(dst)
        if os.path.isdir(dst):
            dst += src

    src = os.path.abspath(src)

    with (open(src, 'rb') as fsrc,
          open(dst, 'wb') as fdst):
        infd, outfd = os.pipe()
        fsrc_size = os.fstat(fsrc.fileno()).st_size

        for _ in range(int(fsrc_size / 65536) + 1):
            os.splice(fsrc.fileno(), outfd, fsrc_size)
            fdst.write(os.read(infd, fsrc_size))

    return dst