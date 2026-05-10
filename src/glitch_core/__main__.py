'''
Glitch.core
Copyright (C) 2026 Savuth

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import sys
import logging
import argparse
import tkinter
from logging import handlers
from datetime import datetime

from . import __version__, g_lgr


hdlBuffer = handlers.MemoryHandler(capacity=1, flushOnClose=False)

def VCrashHandler(tpException, exception, traceback) -> None:
    global hdlBuffer

    g_lgr.critical(f"Uncaught exception: {exception}", exc_info=(exception))

    hdlStdout = logging.StreamHandler()
    hdlStdout.setFormatter(logging.Formatter("[%(levelname)s] (%(threadName)s|%(taskName)s)(%(thread)d)(%(relativeCreated)03d) [%(module)s][%(lineno)d] %(message)s"))

    hdlBuffer.setTarget(hdlStdout)
    hdlBuffer.flush()

def VMain() -> None:
    #TODO: move to logger class
    sys.excepthook = VCrashHandler

    fmt = logging.Formatter("[%(levelname)s] (%(threadName)s|%(taskName)s)(%(thread)d)(%(relativeCreated)03d) [%(module)s][%(lineno)d] %(message)s")
    logging.basicConfig(format=fmt._fmt)

    hdlBuffer.setFormatter(fmt)
    g_lgr.addHandler(hdlBuffer)

    g_lgr.setLevel(logging.DEBUG)

    g_lgr.info("=========")
    g_lgr.info(f"---{sys._getframe().f_code.co_name}")
    g_lgr.info(g_lgr.handlers)

    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--version", action="version", version=__version__)
    parser.parse_args()

    tkinter.Tk()
    tkinter.Label(text=f"{__version__}").pack()

    var = 10/0

    g_lgr.info(f"---Exit {sys._getframe().f_code.co_name}")
    g_lgr.info("=========\n")


# MODULE CALL ENTRY POINT ONLY, NO LOGIC WILL GET RUN ON SCRIPT
if __name__ == "__main__":
    VMain()