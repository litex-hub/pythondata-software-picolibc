import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21414"
version_tuple = (0, 0, 21414)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21414")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21302"
data_version_tuple = (0, 0, 21302)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21302")
except ImportError:
    pass
data_git_hash = "204d4a59723d3a256607741de0f134c3748e2a97"
data_git_describe = "v0.0-21302-g204d4a597"
data_git_msg = """\
commit 204d4a59723d3a256607741de0f134c3748e2a97
Author: Keith Packard <keithp@keithp.com>
Date:   Fri Oct 22 08:58:07 2021 -0700

    doc: Move comment about stdio long long support to paragraph below table
    
    I can't figure out how to get a large text block into a table, so I've
    moved the longer comment about long long support in printf to a
    paragraph below the table of options.
    
    Closes #204.
    
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
