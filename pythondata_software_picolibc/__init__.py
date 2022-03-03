import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post542"
version_tuple = (1, 7, 4, 542)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post542")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post416"
data_version_tuple = (1, 7, 4, 416)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post416")
except ImportError:
    pass
data_git_hash = "f4177d93c29ac06314e78d526d7e280e92a427ff"
data_git_describe = "1.7.4-416-gf4177d93c"
data_git_msg = """\
commit f4177d93c29ac06314e78d526d7e280e92a427ff
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Feb 21 14:28:55 2022 -0800

    .github: Test clang-riscv version
    
    Now that this sample supports testing, run the tests.
    
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
