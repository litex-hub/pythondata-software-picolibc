import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post159"
version_tuple = (1, 7, 9, 159)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post159")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post17"
data_version_tuple = (1, 7, 9, 17)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post17")
except ImportError:
    pass
data_git_hash = "85cdb583c54ca1ab589f92d99648b609b05c7a44"
data_git_describe = "1.7.9-17-g85cdb583c"
data_git_msg = """\
commit 85cdb583c54ca1ab589f92d99648b609b05c7a44
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Oct 20 18:38:08 2022 -0700

    Provide a 'zephyr' mode for errno-function
    
    Select z_errno_wrap when picolibc is configured without thread local
    storage support. Otherwise, place errno in a TLS variable.
    
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
