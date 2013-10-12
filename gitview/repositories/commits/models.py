class Commit(object):
    """
    Wrapper around `git.Commit`.
    """

    def __init__(self, commit, repository=None):
        self.commit = commit
        self.repository = repository


    def __getattr__(self, attr):
        return getattr(self.commit, attr)

    @property
    def committed_time(self):
        from datetime import datetime

        time = datetime.fromtimestamp(self.committed_date)

        return time

    @property
    def description(self):
        lines = self.message.split("\n")

        if lines < 2:
            return ""

        if not lines[1]:
            return "\n".join(lines[2:])

        return "\n".join(lines[1:])

    @property
    def shorthash(self):
        return self.hexsha[:7]