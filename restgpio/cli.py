from restgpio.app import run_app

import argparse
import sys

def webserver_arguments(parser):
    parser.add_argument("--port", default=None, help="Insert the port.")
    parser.add_argument("--host", default=None, help="Insert the host.")
    parser.add_argument(
        "--mode", default=None, type=int, help="Insert board mode, defaults to BCM"
    )
    parser.add_argument(
        "--debug", action="store_true", help="Run in debug mode, all operations are faked."
    )

    for mode in (
        "input",
        "input-pull-up",
        "input-pull-down",
        "output",
        "ouput-low",
        "output-high",
    ):
        parser.add_argument(
            "--" + mode, dest=mode.replace("-", "_"), type=int, nargs="*", default=None
        )

def main(argv=sys.argv[1:], **opts):

    parser = argparse.ArgumentParser(prog="Run a rest api to control GPIO")
    webserver_arguments(parser)

    cmd_options = vars(parser.parse_args(argv))
    args = cmd_options.pop("args", ())
    return run_app(*args, **cmd_options)