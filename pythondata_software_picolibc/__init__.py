import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post587"
version_tuple = (1, 7, 4, 587)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post587")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post461"
data_version_tuple = (1, 7, 4, 461)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post461")
except ImportError:
    pass
data_git_hash = "1c996f43b509fed05bcd61c6eb049c42d57f99c8"
data_git_describe = "1.7.4-461-g1c996f43b"
data_git_msg = """\
commit 1c996f43b509fed05bcd61c6eb049c42d57f99c8
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Mar 7 20:49:30 2022 -0800

    Update COPYING.picolibc
    
    Merged newlib. Replaced ecvtbuf with ecvt_r et al in tinystdio.
    
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
