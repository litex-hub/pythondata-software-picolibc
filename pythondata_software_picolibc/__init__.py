import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21416"
version_tuple = (0, 0, 21416)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21416")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21304"
data_version_tuple = (0, 0, 21304)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21304")
except ImportError:
    pass
data_git_hash = "e8156c004e1b3ffdb046f46e5fb060bb85562f9a"
data_git_describe = "v0.0-21304-ge8156c004"
data_git_msg = """\
commit e8156c004e1b3ffdb046f46e5fb060bb85562f9a
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Thu Oct 21 14:54:41 2021 +0900

    scripts: Replace riscv cpu_family with riscv32 or riscv64
    
    Meson doesn't know riscv as a cpu_family and generate the following
    warning:
    
        WARNING: Unknown CPU family riscv, please report this at
        https://github.com/mesonbuild/meson/issues/new
    
    With the commit c8d139ebb, we now have the CPU family alias table
    installed and can use the CPU families Meson knows.
    
    BTW, I think it's OK for users to use any values but we should use
    what Meson knows.
    
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
