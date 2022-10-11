import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post532"
version_tuple = (1, 7, 8, 532)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post532")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post390"
data_version_tuple = (1, 7, 8, 390)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post390")
except ImportError:
    pass
data_git_hash = "2deb044719eec0e79b5d1bf40e5c4cde0a94a2e8"
data_git_describe = "1.7.8-390-g2deb04471"
data_git_msg = """\
commit 2deb044719eec0e79b5d1bf40e5c4cde0a94a2e8
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 10 09:36:37 2022 -0700

    .github: Build nios2
    
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
