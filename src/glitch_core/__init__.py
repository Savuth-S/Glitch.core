import importlib.metadata
from . import Wrapper

__version__  = importlib.metadata.version(__package__)

g_wrpLogger = Wrapper.Logger()