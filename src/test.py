import unittest

import random
import string
import hashlib
import os
import shutil

from splicecopy import copy

def generate_random_binary_file(size):
    with open(f'tests/src_file_{size}kb', 'wb') as fout:
        fout.write(os.urandom(size))

def md5hash(filename):
    with open(filename,'rb') as fin:
        contents = fin.read()
        return hashlib.md5(contents).hexdigest()

class TestInvalidFiles(unittest.TestCase):
    def test_invalid_sources(self):
        fnames = [''.join(random.choices(string.ascii_uppercase + string.digits, k = 5)) for _ in range(10)]

        for fname in fnames:
            self.assertRaises(FileNotFoundError, copy, fname, 'dst')

class TestCopying(unittest.TestCase):
    def test_md5_integrity(self):
        os.mkdir('tests')
        for size in [2**x for x in range(16)]:
            generate_random_binary_file(size)
            copy(f'tests/src_file_{size}kb', f'tests/dst_file_{size}kb')
            self.assertEqual(md5hash(f'tests/src_file_{size}kb'), md5hash(f'tests/dst_file_{size}kb'))
        shutil.rmtree('tests')

def cleanup():
    if os.path.isdir('tests'):
        shutil.rmtree('tests')

if __name__ == "__main__":
    try:
        unittest.main()
    except KeyboardInterrupt:
        cleanup()