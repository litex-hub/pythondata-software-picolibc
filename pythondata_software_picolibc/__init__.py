import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21560"
version_tuple = (0, 0, 21560)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21560")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21447"
data_version_tuple = (0, 0, 21447)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21447")
except ImportError:
    pass
data_git_hash = "243731a9303374bad23fe2caf10dc1c236af5255"
data_git_describe = "v0.0-21447-g243731a93"
data_git_msg = """\
commit 243731a9303374bad23fe2caf10dc1c236af5255
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Dec 20 14:52:38 2021 -0800

    test: Add tests for char/string put operations
    
    Test fputc, putc, putchar, puts, fputs and fwrite
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post113"
tool_version_tuple = (0, 0, 113)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post113")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
