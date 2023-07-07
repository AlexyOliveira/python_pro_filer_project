from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_with_no_duplicate_files(tmp_path):
    mock_file_path_1 = tmp_path / "no-duplicate1.txt"
    mock_file_path_2 = tmp_path / "no-duplicate2.txt"
    mock_file_path_3 = tmp_path / "no-duplicate3.txt"
    mock_file_path_1.write_text("Lucas")
    mock_file_path_2.write_text("Aline")
    mock_file_path_3.write_text("Luis")

    context = {
        "all_files": [
            str(mock_file_path_1),
            str(mock_file_path_2),
            str(mock_file_path_3),
        ]
    }
    returned = find_duplicate_files(context)

    assert len(returned) == 0


def test_with_duplicate_files(tmp_path):
    mock_file_path_1 = tmp_path / "no-duplicate4.txt"
    mock_file_path_2 = tmp_path / "no-duplicate5.txt"
    mock_file_path_3 = tmp_path / "no-duplicate6.txt"
    mock_file_path_1.write_text("Lucas")
    mock_file_path_2.write_text("Lucas")
    mock_file_path_3.write_text("Lucas")

    context = {
        "all_files": [
            str(mock_file_path_1),
            str(mock_file_path_2),
            str(mock_file_path_3),
        ]
    }
    returned = find_duplicate_files(context)

    assert len(returned) == 3


def test_with_no_file_found(tmp_path, capsys):
    mock_file_path_1 = tmp_path / "no-duplicate4.txt"
    mock_file_path_2 = tmp_path / "no-duplicate5.txt"
    mock_file_path_3 = tmp_path / "no-duplicate6.txt"
    mock_file_path_1.write_text("Lucas")
    mock_file_path_2.write_text("Lucas")

    context = {
        "all_files": [
            str(mock_file_path_1),
            str(mock_file_path_2),
            str(mock_file_path_3),
        ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
