import importlib.metadata
import logging

__version__  = importlib.metadata.version(__package__)

g_lgr = logging.getLogger(__name__)