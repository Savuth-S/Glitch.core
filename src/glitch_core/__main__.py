'''
Glitch.core
Copyright (C) 2026 Savuth

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import sys
import logging
import tkinter

#TODO: setup properly global singleton
logger = logging.getLogger(__name__)

def main() ->None:
    logging.basicConfig(level=logging.DEBUG,
                        format="[%(levelname)s] (%(threadName)s|%(taskName)s)(%(thread)d)(%(relativeCreated)03d) [%(module)s][%(lineno)d] %(message)s")
    logger.info("=========")
    logger.info(f"---{sys._getframe().f_code.co_name}");

    tkinter.Tk()
    tkinter.Label(text="running").pack()
    input()
    logger.info(f"---Exit {sys._getframe().f_code.co_name}");
    logger.info("=========\n");

if __name__ == "__main__":
    main()