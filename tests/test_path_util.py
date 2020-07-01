

from pathlib import Path as Pathlib

import path_util
from path_util import Path


def test_path_util(tmp_path: Pathlib):

    path = str(tmp_path.joinpath('one', 'file.txt'))
    path_util.create_path(path)

    assert Pathlib(path).exists()
    assert Pathlib(path).is_file()


def test_path_exists(tmp_path: Pathlib):

    path = str(tmp_path.joinpath('one', 'file.txt'))
    path_util.create_path(path)

    assert Path(path).exists



