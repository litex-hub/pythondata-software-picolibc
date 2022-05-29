import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post143"
version_tuple = (1, 7, 7, 143)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post143")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post3"
data_version_tuple = (1, 7, 7, 3)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post3")
except ImportError:
    pass
data_git_hash = "419ac5cd358d7e12dd63e0b2c46cd03a366956ac"
data_git_describe = "1.7.7-3-g419ac5cd3"
data_git_msg = """\
commit 419ac5cd358d7e12dd63e0b2c46cd03a366956ac
Author: Keith Packard <keithp@keithp.com>
Date:   Mon May 23 21:37:50 2022 -0700

    testsuite/newlib.stdio: Make swprintf 'main' a modern function
    
    Add '(void)' parameters
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
