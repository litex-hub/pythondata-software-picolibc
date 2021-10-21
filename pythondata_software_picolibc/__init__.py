import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21413"
version_tuple = (0, 0, 21413)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21413")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21301"
data_version_tuple = (0, 0, 21301)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21301")
except ImportError:
    pass
data_git_hash = "2bd4d764deb542e4a8650b60cb250870b0a4f4e7"
data_git_describe = "v0.0-21301-g2bd4d764d"
data_git_msg = """\
commit 2bd4d764deb542e4a8650b60cb250870b0a4f4e7
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Thu Oct 21 11:31:24 2021 +0900

    meson.build: Move get_option() at conf_data.set()
    
    Directly call get_option() at conf_data.set() if an option is only
    used to set the configuration data.  This reduces the number of
    variables to worry about.
    
    No functionality should have been changed.
    
    Signed-off-by: Yasushi SHOJI <yashi@spacecubics.com>

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
