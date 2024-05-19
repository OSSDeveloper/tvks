import os

def get_os_agnostic_path(*rel_paths):
    """
    Returns an OS-agnostic path from the current directory.

    Args:
        *rel_paths: One or more relative paths as strings.

    Returns:
        str: OS-agnostic path from the current directory.
    """
    current_dir = os.getcwd()
    path = current_dir
    for rel_path in rel_paths:
        path = os.path.join(path, rel_path)
    return path