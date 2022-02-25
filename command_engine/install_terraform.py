"""
This script defines the entry point for terra-install.
"""
import subprocess


def main() -> None:
    """
    Runs the installation script for terraform.

    :return: None
    """
    print("installing terraform")
    subprocess.call("./scripts/install_terraform.sh")
