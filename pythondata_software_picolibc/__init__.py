import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21353"
version_tuple = (0, 0, 21353)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21353")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21241"
data_version_tuple = (0, 0, 21241)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21241")
except ImportError:
    pass
data_git_hash = "944aab1f4418e3e436e9cc70b0c904ada4e017d8"
data_git_describe = "v0.0-21241-g944aab1f4"
data_git_msg = """\
commit 944aab1f4418e3e436e9cc70b0c904ada4e017d8
Author: Keith Packard <keithp@keithp.com>
Date:   Fri Oct 8 11:25:01 2021 -0700

    scripts: GCC in testing has updated to 10.3.1
    
    This means the clang builds need to change the path to libgcc
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
