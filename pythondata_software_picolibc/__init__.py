import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post152"
version_tuple = (1, 7, 9, 152)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post152")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post10"
data_version_tuple = (1, 7, 9, 10)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post10")
except ImportError:
    pass
data_git_hash = "8a98d4d6b5c9ae43d6a980bfd5678fe88fbdf35c"
data_git_describe = "1.7.9-10-g8a98d4d6b"
data_git_msg = """\
commit 8a98d4d6b5c9ae43d6a980bfd5678fe88fbdf35c
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Oct 19 10:33:39 2022 -0700

    xtensa: Add _set_tls helper
    
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
