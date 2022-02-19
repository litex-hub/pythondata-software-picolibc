import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post493"
version_tuple = (1, 7, 4, 493)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post493")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post367"
data_version_tuple = (1, 7, 4, 367)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post367")
except ImportError:
    pass
data_git_hash = "cea19312063fbe42d1388179d09e1102feb85918"
data_git_describe = "1.7.4-367-gcea193120"
data_git_msg = """\
commit cea19312063fbe42d1388179d09e1102feb85918
Author: Keith Packard <keithp@keithp.com>
Date:   Sun Feb 13 23:28:20 2022 -0800

    test: Ignore -Wstringop-truncation when building printf_scanf
    
    This test triggers a warning when using strncpy in valid, if slightly
    unusual way.
    
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
