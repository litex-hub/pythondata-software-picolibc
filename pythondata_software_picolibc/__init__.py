import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post151"
version_tuple = (1, 7, 9, 151)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post151")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post9"
data_version_tuple = (1, 7, 9, 9)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post9")
except ImportError:
    pass
data_git_hash = "28db410e56cc9eeed0f6ef493aea26755ef644e1"
data_git_describe = "1.7.9-9-g28db410e5"
data_git_msg = """\
commit 28db410e56cc9eeed0f6ef493aea26755ef644e1
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Oct 19 08:58:44 2022 -0700

    .github: Build arc configurations in CI
    
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
