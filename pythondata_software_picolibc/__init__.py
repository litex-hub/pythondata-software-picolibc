import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post433"
version_tuple = (1, 7, 6, 433)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post433")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post305"
data_version_tuple = (1, 7, 6, 305)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post305")
except ImportError:
    pass
data_git_hash = "f721a3514a3656ee0c7493ee17c88122dfbaa263"
data_git_describe = "1.7.6-305-gf721a3514"
data_git_msg = """\
commit f721a3514a3656ee0c7493ee17c88122dfbaa263
Author: Keith Packard <keithp@keithp.com>
Date:   Wed May 18 14:47:37 2022 -0700

    semihost: Add stdint.h to semihost.h
    
    Now that stdint.h doesn't get included by other headers, we need to
    include it explicitly where used.
    
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
