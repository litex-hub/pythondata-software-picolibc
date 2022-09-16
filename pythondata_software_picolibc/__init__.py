import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post473"
version_tuple = (1, 7, 8, 473)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post473")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post331"
data_version_tuple = (1, 7, 8, 331)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post331")
except ImportError:
    pass
data_git_hash = "5c5f2a2e2a46066fafae38d228e1550339578fd0"
data_git_describe = "1.7.8-331-g5c5f2a2e2"
data_git_msg = """\
commit 5c5f2a2e2a46066fafae38d228e1550339578fd0
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Sep 14 15:35:19 2022 +0100

    .github: Build MSP430 bits
    
    Use the TI MSP430 GNU SDK to build using both clang and gcc.
    
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
