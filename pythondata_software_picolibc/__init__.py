import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21508"
version_tuple = (0, 0, 21508)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21508")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21396"
data_version_tuple = (0, 0, 21396)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21396")
except ImportError:
    pass
data_git_hash = "c078c27985cdc8617096cd04f683f7c2e19f4b64"
data_git_describe = "v0.0-21396-gc078c2798"
data_git_msg = """\
commit c078c27985cdc8617096cd04f683f7c2e19f4b64
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Nov 3 21:56:46 2021 -0700

    xdr: Silence compiler warning about uninitialized variable
    
    'size' will be set in the ENCODE path, but the compiler can't tell, so
    just initialize it always.
    
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
