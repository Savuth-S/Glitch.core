'''
Glitch.core
Copyright (C) 2026 Savuth

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import sys
import argparse
import tkinter
import logging
from datetime import datetime

from . import g_wrpLogger, __version__, Wrapper


def VMain() -> None:
    # g_wrpLogger.VSetStdOutLevel(logging.CRITICAL)

    g_wrpLogger.info("=========")
    g_wrpLogger.info(f"---{sys._getframe().f_code.co_name}")

    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--version", action="version", version=__version__)
    parser.parse_args()

    tkinter.Tk()
    tkinter.Label(text=f"{__version__}").pack()

    g_wrpLogger.info(f"---Exit {sys._getframe().f_code.co_name}")
    g_wrpLogger.info("=========\n")


# MODULE CALL ENTRY POINT ONLY, NO LOGIC WILL GET RUN ON SCRIPT
if __name__ == "__main__":
    VMain()