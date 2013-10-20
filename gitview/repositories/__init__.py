REPOSITORY_REGEX = r"(?P<owner_name>[-\w]+)/(?P<repository_name>[-\w]+)"

COMMIT_REGEX = r"(?P<commit_hash>[a-f0-9]{7,40})"

TREE_REGEX = r"(?P<tree_name>[-\w]+)"

TREE_PATH_REGEX = r"(?P<tree_path>.+)"
