import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post349"
version_tuple = (1, 7, 4, 349)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post349")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post225"
data_version_tuple = (1, 7, 4, 225)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post225")
except ImportError:
    pass
data_git_hash = "380d1af3dafcf25e705a25636c17e62b8b835b29"
data_git_describe = "1.7.4-225-g380d1af3d"
data_git_msg = """\
commit 380d1af3dafcf25e705a25636c17e62b8b835b29
Author: Keith Packard <keithp@keithp.com>
Date:   Sun Feb 6 13:24:32 2022 -0800

    .github: Remove unneeded packages from each workflow
    
    This should make the cache files a bit more reasonably sized.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
