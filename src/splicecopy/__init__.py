import os
import sys

class IsDirectoryError(Exception):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"{self.filename} is a directory.")

class InvalidPlatformError(Exception):
    def __init__(self):
        super().__init__(f"Invalid Platform. Requires Linux with Python >=3.10.")

# `os.splice()` is only available on Linux and Python >=3.10
_HAS_OS_SPLICE = hasattr(os, "splice") and sys.platform.startswith("linux")

def copy(src: str, dst: str) -> str: 
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
        read_fd, write_fd = os.pipe()
        for _ in range(int(os.path.getsize(src) / 65536) + 1):
            os.splice(fsrc.fileno(), write_fd, os.path.getsize(src))
            fdst.write(os.read(read_fd, os.path.getsize(src)))

    return dst