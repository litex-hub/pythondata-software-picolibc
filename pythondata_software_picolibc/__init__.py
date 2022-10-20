import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post153"
version_tuple = (1, 7, 9, 153)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post153")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post11"
data_version_tuple = (1, 7, 9, 11)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post11")
except ImportError:
    pass
data_git_hash = "67574211585540c048ccc5df5f46a37055e2eb5d"
data_git_describe = "1.7.9-11-g675742115"
data_git_msg = """\
commit 67574211585540c048ccc5df5f46a37055e2eb5d
Author: Troels Jessen <troels@space-inventor.com>
Date:   Fri Sep 30 09:48:00 2022 +0200

    Remove double underscores in defines
    
    Defines with double underscores does not exist for all compilers,
    causing environment to default to big endian

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
