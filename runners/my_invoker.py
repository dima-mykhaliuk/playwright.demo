import pytest
import os

if __name__ == "__main__":
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    root_dir = parent_dir
    tests_dir = os.path.join(root_dir, "tests")

    pytest.main(["-v", f"--rootdir={root_dir}", "--pyargs", tests_dir])
