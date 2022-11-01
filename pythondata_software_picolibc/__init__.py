import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post177"
version_tuple = (1, 7, 9, 177)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post177")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post35"
data_version_tuple = (1, 7, 9, 35)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post35")
except ImportError:
    pass
data_git_hash = "d1bf7cdb736399c2e8fd182f1eb887b2d2e471a2"
data_git_describe = "1.7.9-35-gd1bf7cdb7"
data_git_msg = """\
commit d1bf7cdb736399c2e8fd182f1eb887b2d2e471a2
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 31 18:17:18 2022 -0700

    tinystdio: Add strto*l_l functions
    
    These take a locale pointer, which is ignored. Used by
    strptime.
    
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
