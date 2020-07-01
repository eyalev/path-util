

from pathlib import Path

import path_util


def test_path_util(tmp_path: Path):

    path = str(tmp_path.joinpath('one', 'file.txt'))
    path_util.create_path(path)

    assert Path(path).exists()
    assert Path(path).is_file()

