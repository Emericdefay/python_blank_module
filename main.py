#!/D:/Sauvegarde/Developpeur/K0rp/blank_module/env/Scripts python

# Std. libraries
import argparse

# Installed libraries
# [...]

# Local libraries
from functions import index

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programm description")
    parser.add_argument("command", help="dummy function")
    parser.add_argument("-p", "--parameter", type=int, help="Very important parameter")
    args = parser.parse_args()

    # Index of commands available
    index.commands.get(args.command, index.default)(args.parameter)
