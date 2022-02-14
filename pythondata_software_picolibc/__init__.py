import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post363"
version_tuple = (1, 7, 4, 363)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post363")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post237"
data_version_tuple = (1, 7, 4, 237)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post237")
except ImportError:
    pass
data_git_hash = "6de1d3fd14f642ed624089a13f5dff7aa8cb4f23"
data_git_describe = "1.7.4-237-g6de1d3fd1"
data_git_msg = """\
commit 6de1d3fd14f642ed624089a13f5dff7aa8cb4f23
Author: Johan de Claville Christiansen <johan@space-inventor.com>
Date:   Sun Feb 13 17:16:25 2022 +0100

    meson: run_command set check to false on expr

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
