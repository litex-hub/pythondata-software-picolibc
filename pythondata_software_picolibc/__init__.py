import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post184"
version_tuple = (1, 7, 6, 184)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post184")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post56"
data_version_tuple = (1, 7, 6, 56)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post56")
except ImportError:
    pass
data_git_hash = "c60f7e0c32f5cbd16757e1899fecd350ba168a78"
data_git_describe = "1.7.6-56-gc60f7e0c3"
data_git_msg = """\
commit c60f7e0c32f5cbd16757e1899fecd350ba168a78
Author: Keith Packard <keithp@keithp.com>
Date:   Tue May 17 16:03:10 2022 -0700

    .github: Add a cmake test
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
