"""
Python wrapper for tw pipelines command
"""
from .utils import tw_run
from pathlib import Path

# Tagging for code review on 06/07/2023
# This entire script is very much undone and needs to be finished
# I started modelling it out to contain mainly workspace/org setup methods
# Can probably be split into multiple classes?


class Workspace:
    """
    Python wrapper for tw pipelines command
    """

    cmd = "pipelines"

    def __init__(self, workspace_name):
        self.workspace = workspace_name

    def _tw_run(self, command, *args, **kwargs):
        return tw_run(command, *args, **kwargs)

    def list(self, *args, **kwargs):
        """
        List workspaces
        """
        return self._tw_run(
            [self.cmd, "list", "--workspace", self.workspace], *args, **kwargs
        )

    def delete(self, name, *args, **kwargs):
        """
        Delete a workspace
        """
        self._tw_run([self.cmd, "delete", "--name", name], *args, **kwargs)

    def add(self, name, organization, *args, **kwargs):
        """
        Add a workspace
        """
        self._tw_run(
            [
                self.cmd,
                "add",
                "--name",
                name,
                organization,
            ],
            *args,
            **kwargs,
        )

    def update(self, name, *args, **kwargs):
        """
        Update a workspace
        """
        return self._tw_run([self.cmd, "list", "--workspace", name], *args, **kwargs)

    # TODO: leave a workspace
