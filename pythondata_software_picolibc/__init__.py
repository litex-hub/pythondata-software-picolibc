import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post156"
version_tuple = (1, 7, 7, 156)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post156")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post14"
data_version_tuple = (1, 7, 7, 14)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post14")
except ImportError:
    pass
data_git_hash = "e87b2fc37345a62361478f0a6efd140e14180ba5"
data_git_describe = "1.7.7-14-ge87b2fc37"
data_git_msg = """\
commit e87b2fc37345a62361478f0a6efd140e14180ba5
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Jun 22 11:08:35 2022 -0700

    cmake: Allow setting of __PICOLIBC_ERRNO_FUNCTION
    
    This is needed for non-TLS builds of Zephyr.
    
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
