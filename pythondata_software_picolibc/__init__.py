import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post142"
version_tuple = (1, 7, 6, 142)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post142")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post16"
data_version_tuple = (1, 7, 6, 16)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post16")
except ImportError:
    pass
data_git_hash = "af27334b30bf9192a1984f4f1e6a661f18867e4f"
data_git_describe = "1.7.6-16-gaf27334b3"
data_git_msg = """\
commit af27334b30bf9192a1984f4f1e6a661f18867e4f
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Apr 12 09:40:58 2022 -0700

    tinystdio: Ignore thousands separator flag
    
    POSIX defines a thousands separator flag for printf, ', which causes
    the current locale thousands separator to be placed between groups of
    digits to make them easier to read. As tinystdio doesn't have any
    locale support, and as the C/POSIX locale has an empty thousands
    separator, we can "support" this feature by simply ignoring this flag.
    
    Enabling this feature in a useful fashion will require either some
    level of locale support or creating a custom API to control it.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

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
