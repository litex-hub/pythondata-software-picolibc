import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post346"
version_tuple = (1, 7, 4, 346)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post346")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post222"
data_version_tuple = (1, 7, 4, 222)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post222")
except ImportError:
    pass
data_git_hash = "a8ae5ad10df0b14c0b5ab34d7b67d25ede317bdb"
data_git_describe = "1.7.4-222-ga8ae5ad10"
data_git_msg = """\
commit a8ae5ad10df0b14c0b5ab34d7b67d25ede317bdb
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Wed Jan 26 14:53:56 2022 +0900

    meson.build: Fix description keyword in configuration set()
    
    There are two typo for the keyword 'description' for config data set()
    in meson.build.
    
    Meson 0.61 doesn't warn about this but a post v0.61 with the
    commit mesonbuild/meson/commit/574525673f6 will error out with:
    
       meson.build:737:10: ERROR: configuration_data.set got unknown
       keyword arguments "descrption"
    
    This is reported by @tcal-x.
    
    Closes #244.
    
    Signed-off-by: Yasushi SHOJI <yashi@spacecubics.com>

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
