#!/usr/bin/env python3
import os

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_file(f_name):
    os.remove(f_name)

def main():
    linter = "{{ cookiecutter.linter }}".lower()
    if linter == "flake8":
        remove_file(".pylintrc")
    if linter == "pylint":
        remove_file(".flake8")

    print(f"{SUCCESS} Project initialized, keep up the good work!{TERMINATOR}")


if __name__ == "__main__":
    main()
