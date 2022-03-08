import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post583"
version_tuple = (1, 7, 4, 583)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post583")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post457"
data_version_tuple = (1, 7, 4, 457)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post457")
except ImportError:
    pass
data_git_hash = "a268b62a21c9f9d2517ba5fcbbe00c6337ee9cd5"
data_git_describe = "1.7.4-457-ga268b62a2"
data_git_msg = """\
commit a268b62a21c9f9d2517ba5fcbbe00c6337ee9cd5
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Mar 7 14:46:50 2022 -0800

    math: Do nexttowardf nan exceptions in float instead of long double
    
    nexttowardf was performing the nan exception conversion using long
    double, which only works correctly if the target exception handling is
    the same for float and long double.
    
    Switch this function to doing the computation in floats instead, which
    is a bit tricky because converting a sNaN long double to float returns
    qNaN, but only raises INVALID if the target supports exceptions on
    long double. Instead, manually convert a signaling long double to a
    signaling float.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
