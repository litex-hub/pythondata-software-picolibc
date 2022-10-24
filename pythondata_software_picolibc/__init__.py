import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post164"
version_tuple = (1, 7, 9, 164)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post164")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post22"
data_version_tuple = (1, 7, 9, 22)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post22")
except ImportError:
    pass
data_git_hash = "e2d558295bed357cb6ec47a545533afb9d7151fe"
data_git_describe = "1.7.9-22-ge2d558295"
data_git_msg = """\
commit e2d558295bed357cb6ec47a545533afb9d7151fe
Author: Keith Packard <keithp@keithp.com>
Date:   Sun Oct 23 14:13:04 2022 -0700

    test: Exhaustively test strtol in-range/out-of-range parsing
    
    Make sure strtol deals with every possible character value correctly,
    assigning it to be either in-range or out-of-range.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
