import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post148"
version_tuple = (1, 7, 7, 148)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post148")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post6"
data_version_tuple = (1, 7, 7, 6)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post6")
except ImportError:
    pass
data_git_hash = "575808225cc3fa60e76a07e88e7862c77cf6842b"
data_git_describe = "1.7.7-6-g575808225"
data_git_msg = """\
commit 575808225cc3fa60e76a07e88e7862c77cf6842b
Author: Keith Packard <keithp@keithp.com>
Date:   Sun Jun 19 11:25:15 2022 -0700

    Fix formatting in README.md
    
    Use literal mode for a couple of prefixes both to make it clear that
    it's code and to avoid interpreting the __ as formatting.
    
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
