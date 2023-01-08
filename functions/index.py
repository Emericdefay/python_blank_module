# Std. libraries
# [...]

# Installed libraries
# [...]

# Local libraries
from .specific import (
    dummy,
)


def default():
    print("Unknown command")


commands = {
    "dummy": dummy.dummy_function,
}
