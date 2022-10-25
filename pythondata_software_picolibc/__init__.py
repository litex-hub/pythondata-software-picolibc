import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post165"
version_tuple = (1, 7, 9, 165)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post165")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post23"
data_version_tuple = (1, 7, 9, 23)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post23")
except ImportError:
    pass
data_git_hash = "16a3a470be97e01d3edd3b5161fcb350c5a71681"
data_git_describe = "1.7.9-23-g16a3a470b"
data_git_msg = """\
commit 16a3a470be97e01d3edd3b5161fcb350c5a71681
Author: Ryan McClelland <ryanmcclelland@meta.com>
Date:   Mon Oct 24 00:25:24 2022 -0700

    fix -Werror=double-promotion issues
    
    When compiling with the gcc flag -Werror=double-promotion.
    Three errors are given which are implicit conversion from float
    to double to match other result of the conditional

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
