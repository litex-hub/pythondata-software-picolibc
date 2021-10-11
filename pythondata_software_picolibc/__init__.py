import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21369"
version_tuple = (0, 0, 21369)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21369")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21257"
data_version_tuple = (0, 0, 21257)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21257")
except ImportError:
    pass
data_git_hash = "9463f4b62e703308c9be4a599bd5de63dd01492c"
data_git_describe = "v0.0-21257-g9463f4b62"
data_git_msg = """\
commit 9463f4b62e703308c9be4a599bd5de63dd01492c
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Sat Oct 9 05:55:47 2021 +0900

    gitignore: Remove config.h
    
    This entry matches all "config.h" in the tree.  We actually have
    "config.h" in the tree right now.
    
      - newlib/libc/include/sys/config.h
    
    Modern tools, such as the Silver Searcher or Ripgrep, check .gitignore
    and drop matched files and directories.  That means, we are hiding the
    actual files.
    
    The .gitignore is inherited from Newlib and have many files from the
    GNU Autotools era.  Removing config.h doesn't hurt picolibc
    development.
    
    We can specifically ignore config.h in the root directory with
    '/config.h' but decided to simply remove it.
    
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
