import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post158"
version_tuple = (1, 7, 7, 158)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post158")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post16"
data_version_tuple = (1, 7, 7, 16)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post16")
except ImportError:
    pass
data_git_hash = "ce7bd3ba2761497ba380cb131d1493eb7c2bcaab"
data_git_describe = "1.7.7-16-gce7bd3ba2"
data_git_msg = """\
commit ce7bd3ba2761497ba380cb131d1493eb7c2bcaab
Author: Keith Packard <keithp@keithp.com>
Date:   Fri Jun 24 17:10:05 2022 -0700

    Add basic arc/arc64 support
    
    Add meson and cmake scripts for the machine-specific 32-bit arc code.
    Add scripts to build using the Zephyr toolchain.
    
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
