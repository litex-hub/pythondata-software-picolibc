import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post483"
version_tuple = (1, 7, 8, 483)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post483")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post341"
data_version_tuple = (1, 7, 8, 341)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post341")
except ImportError:
    pass
data_git_hash = "2508101bf38b09c5255798107b59ee2bc7474f69"
data_git_describe = "1.7.8-341-g2508101bf"
data_git_msg = """\
commit 2508101bf38b09c5255798107b59ee2bc7474f69
Author: Keith Packard <keithp@keithp.com>
Date:   Sat Oct 8 16:59:41 2022 -0700

    .github: List installed packages
    
    Try to debug libgcc errors
    
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
