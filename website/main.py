# Standard Library
import argparse
from importlib import import_module

APP = import_module('app')


def main():
    """Drive application upon startup and setup environment."""
    current_exit_code = 0
    app = APP.Website()

    # Closure to ensure information window opens after the
    # event loop is started
    def on_start_cb():
        app.init()
    if current_exit_code == 0:
        on_start_cb()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='Petes Meals', description='Main Website.')

    args = parser.parse_args()
    main()

