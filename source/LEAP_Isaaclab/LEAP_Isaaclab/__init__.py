"""
Python module serving as a project/extension template.
"""

# Register Gym environments.
from .tasks import *

# Register UI extensions only when running inside an Omniverse/Isaac Sim runtime.
try:
    from .ui_extension_example import *
except ModuleNotFoundError:
    pass
