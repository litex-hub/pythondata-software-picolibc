import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post133"
version_tuple = (1, 7, 6, 133)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post133")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post7"
data_version_tuple = (1, 7, 6, 7)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post7")
except ImportError:
    pass
data_git_hash = "a1bb47818d2f2b0f76d37b5fe1a795f3a8f6c794"
data_git_describe = "1.7.6-7-ga1bb47818"
data_git_msg = """\
commit a1bb47818d2f2b0f76d37b5fe1a795f3a8f6c794
Merge: b1aae1165 816b10551
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Apr 4 10:12:52 2022 -0700

    Merge remote-tracking branch 'rdiez/patch-3'

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
