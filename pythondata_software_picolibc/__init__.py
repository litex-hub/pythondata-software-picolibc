import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21408"
version_tuple = (0, 0, 21408)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21408")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21296"
data_version_tuple = (0, 0, 21296)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21296")
except ImportError:
    pass
data_git_hash = "703aec6a83696097ec598cf21344243002b0e123"
data_git_describe = "v0.0-21296-g703aec6a8"
data_git_msg = """\
commit 703aec6a83696097ec598cf21344243002b0e123
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 18 12:09:18 2021 -0700

    .github: Replace use of apt-key with file in trusted.gpg.d
    
    apt-key is deprecated and can be replaced by putting the new key in
    /etc/apt/trusted.gpg.d instead. Do this by having wget write to that
    file.
    
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
