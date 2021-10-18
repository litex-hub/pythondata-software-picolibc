import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21394"
version_tuple = (0, 0, 21394)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21394")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21282"
data_version_tuple = (0, 0, 21282)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21282")
except ImportError:
    pass
data_git_hash = "27e7610aae25917fbf54e7222a77af382558ac88"
data_git_describe = "v0.0-21282-g27e7610aa"
data_git_msg = """\
commit 27e7610aae25917fbf54e7222a77af382558ac88
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Sat Oct 16 00:18:30 2021 +0900

    github/Dockerfile: Use packages.txt to have a list of packages
    
    Having a list of packages in Dockerfile is something we all do.  But
    it's not readable when we have multiple retries.  Extract the list to
    a text file and copy it to the container before the build.  This is
    much more readable and gives us a single list to change.
    
    We don't really care about additional layer created by the COPY
    instruction because we aren't shipping the docker image.
    
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
