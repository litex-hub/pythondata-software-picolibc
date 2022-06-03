import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post146"
version_tuple = (1, 7, 7, 146)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post146")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post4"
data_version_tuple = (1, 7, 7, 4)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post4")
except ImportError:
    pass
data_git_hash = "579710373351530f3614389cbb1dc1f3f2085b56"
data_git_describe = "1.7.7-4-g579710373"
data_git_msg = """\
commit 579710373351530f3614389cbb1dc1f3f2085b56
Author: Max Behensky <maxb@twinlanes.com>
Date:   Thu Jun 2 16:49:04 2022 -0700

    Fix issues with out of source build CMake install.
    
    The picolibc.specs file lives in the build directory, not the source directory.
    The picolibc.h file wasn't getting copied to the install include directory.

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
