import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post146"
version_tuple = (1, 7, 9, 146)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post146")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post4"
data_version_tuple = (1, 7, 9, 4)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post4")
except ImportError:
    pass
data_git_hash = "481c4b5ac4781d2fbba8c1cf66fe7da48d4a831b"
data_git_describe = "1.7.9-4-g481c4b5ac"
data_git_msg = """\
commit 481c4b5ac4781d2fbba8c1cf66fe7da48d4a831b
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Oct 13 23:17:49 2022 -0700

    cmake: Skip asm code on arcv3
    
    The accelerated asm code only works on older arc targets, just use the
    C code versions on new hardware. This already worked with meson, which
    checks a CPP symbol. The cmake bits use CONFIG values instead.
    
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
