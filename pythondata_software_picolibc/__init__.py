import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post148"
version_tuple = (1, 7, 4, 148)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post148")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post27"
data_version_tuple = (1, 7, 4, 27)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post27")
except ImportError:
    pass
data_git_hash = "29d7282a37fca022c8ea3214f53f0dbcc5173b63"
data_git_describe = "1.7.4-27-g29d7282a3"
data_git_msg = """\
commit 29d7282a37fca022c8ea3214f53f0dbcc5173b63
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Jan 3 11:03:12 2022 -0800

    Add double-underscore PICOLIBC version macros
    
    When I initially created the meson build files, I mistakenly used only
    a single leading underscore in all of the version macros. This adds
    double leading underscore names, leaving the single underscore names
    for anyone using them.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post121"
tool_version_tuple = (0, 0, 121)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post121")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
