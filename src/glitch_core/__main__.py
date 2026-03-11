'''
Glitch.core
Copyright (C) 2026 Savuth

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
import sys
import logging

def main() ->None:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    print("running")
    logger.debug("test")


if __name__ == "__main__":
    main()