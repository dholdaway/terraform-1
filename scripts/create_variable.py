"""
This script creates an environment variable for terraform
"""
from subprocess import Popen
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("variable_name", help="The name of the variable being inserted", type=str)
    parser.add_argument("variable_value", help="The value of the variable being inserted", type=str)
    args = parser.parse_args()

    create_process = Popen(f"export TF_VAR_{args.variable_name}={args.variable_value}", shell=True)
    create_process.wait()
