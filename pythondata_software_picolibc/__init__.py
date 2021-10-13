import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21373"
version_tuple = (0, 0, 21373)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21373")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21261"
data_version_tuple = (0, 0, 21261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21261")
except ImportError:
    pass
data_git_hash = "412a126f568f84e2723566e9065826a9bcbefd4a"
data_git_describe = "v0.0-21261-g412a126f5"
data_git_msg = """\
commit 412a126f568f84e2723566e9065826a9bcbefd4a
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Tue Oct 12 23:20:19 2021 +0900

    scripts: Modernize meson usage in do-*-configure
    
    Use 'meson setup' style instead of the old 'meson <sourcedir>' which
    predates meson version 0.42.
    
    This also let us specify the builddir in the following form:
    
      ./scripts/do-riscv-configure builddir
    
    This might be handy when you want to build many arch in one go,
    without mkdir-cd dance.
    
    This change keeps the backward compatibility and doesn't break the
    current scripts.
    
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
