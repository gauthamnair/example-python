from platform import platform

import os

def test_platform():
    assert ('hello1', 'b') == (platform(), os.getenv('CFG', '__'))

