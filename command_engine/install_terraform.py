"""
This script defines the entry point for terra-install.
"""
import subprocess
from pathlib import Path


def main() -> None:
    """
    Runs the installation script for terraform.

    :return: None
    """
    print("installing terraform")
    subprocess.call(f"{str(Path(__file__).parent)}/scripts/install_terraform.sh")
