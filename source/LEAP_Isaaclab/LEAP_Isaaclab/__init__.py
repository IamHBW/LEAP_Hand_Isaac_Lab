"""
Python module serving as a project/extension template.
"""

from importlib.util import find_spec

# Register Gym environments.
from .tasks import *

# Register UI extensions only when running inside an Omniverse/Isaac Sim runtime.
if find_spec("omni.ext") is not None:
    from .ui_extension_example import *
