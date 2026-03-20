"""
Script to print all the available LEAP environments in the extension.
"""

import gymnasium as gym
from prettytable import PrettyTable

import LEAP_Isaaclab.tasks  # noqa: F401


def main():
    table = PrettyTable(["S. No.", "Task Name", "Entry Point", "Config"])
    table.title = "Available LEAP Environments"
    table.align["Task Name"] = "l"
    table.align["Entry Point"] = "l"
    table.align["Config"] = "l"

    index = 0
    for task_spec in gym.registry.values():
        if task_spec.id.startswith("Isaac-Reorient-Cube-Leap"):
            table.add_row([index + 1, task_spec.id, task_spec.entry_point, task_spec.kwargs["env_cfg_entry_point"]])
            index += 1

    print(table)


if __name__ == "__main__":
    main()
