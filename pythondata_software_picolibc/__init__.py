import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post141"
version_tuple = (1, 7, 6, 141)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post141")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post15"
data_version_tuple = (1, 7, 6, 15)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post15")
except ImportError:
    pass
data_git_hash = "4068b85b9b48566caee79d66b1f9bac79f728a8c"
data_git_describe = "1.7.6-15-g4068b85b9"
data_git_msg = """\
commit 4068b85b9b48566caee79d66b1f9bac79f728a8c
Merge: 2ffcc0768 2efd2d18f
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Apr 12 10:10:53 2022 -0700

    Merge remote-tracking branch 'aykevl/fix-16-bit-int-shift'

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
