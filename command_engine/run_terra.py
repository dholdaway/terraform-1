"""
This script defines the entry point for terra-apply.
"""
import os
from pathlib import Path
from subprocess import Popen

from command_engine.config_loader import ConfigEngine


def main() -> None:
    """
    Loads the data from the terra_config.yml config file in the current directory and run a terraform apply command.

    :return: None
    """
    config_path: str = str(os.getcwd()) + "/terra_config.yml"
    file_path: str = str(Path(__file__).parent)

    config = ConfigEngine(config_path=config_path)

    command_buffer = [f'cd {file_path}/{config["location"]} ', '&& ', 'terraform apply ']
    variables = config["variables"]

    for key in variables:
        command_buffer.append(f'-var="{key}={variables[key]}" ')

    command = "".join(command_buffer)
    print("applying the following command: ")
    print(command)

    continue_running = input("please type 'yes': ")
    if continue_running == "yes":
        run_terraform = Popen(command, shell=True)
        run_terraform.wait()
