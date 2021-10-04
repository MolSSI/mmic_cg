"""
mmic_cg
A generic component for coarse-graining
"""

# Add imports here
# from .mmic_mmic_cg import *
from . import models, components
from .models import *
from .components import *

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
