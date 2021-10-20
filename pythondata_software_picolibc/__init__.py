import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21409"
version_tuple = (0, 0, 21409)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21409")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21297"
data_version_tuple = (0, 0, 21297)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21297")
except ImportError:
    pass
data_git_hash = "d381e5d8d89bdea9b900efbfa13afa04b20af113"
data_git_describe = "v0.0-21297-gd381e5d8d"
data_git_msg = """\
commit d381e5d8d89bdea9b900efbfa13afa04b20af113
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Wed Oct 20 23:13:00 2021 +0900

    github/workflows: Disable gha cache backend
    
    I can't make this experimental GitHub Actions cache exporter backend
    work reliably with build-push-action.  Disable it for now.
    
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
