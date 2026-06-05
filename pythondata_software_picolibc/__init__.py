import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/litex-hub/picolibc"

# Module version
version_str = "1.8.11.post1"
version_tuple = (1, 8, 11, 1)
try:
    from packaging.version import Version as V
    pversion = V("1.8.11.post1")
except ImportError:
    pass

# Data version info
data_version_str = "1.8.11.post1"
data_version_tuple = (1, 8, 11, 1)
try:
    from packaging.version import Version as V
    pdata_version = V("1.8.11.post1")
except ImportError:
    pass
data_git_hash = "16ff442da4b92e28d0753fabed18ad4a15254498"
data_git_describe = "1.8.11-1-g16ff442da"
data_git_msg = """\
commit 16ff442da4b92e28d0753fabed18ad4a15254498
Author: Florent Kermarrec <florent@enjoy-digital.fr>
Date:   Fri Jun 5 13:13:43 2026 +0200

    meson: Alias PPC CPU family to PowerPC
    
    Meson uses ppc as the canonical CPU family name for 32-bit PowerPC, while picolibc machine support lives under libc/machine/powerpc. Add the missing alias so cross files using cpu_family='ppc' select the existing PowerPC backend instead of failing with Unsupported architecture: ppc.
    
    The 32-bit PowerPC setjmp path and endian macros are already fixed in current picolibc; this addresses the remaining family-name mismatch reported in enjoy-digital/litex#1400.

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
