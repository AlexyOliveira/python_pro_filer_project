from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import patch, Mock


def test_if_show_disk_usage_shows_the_info_files_correctly(capsys, tmp_path):
    mock__get_printable_file_path = Mock()
    mock_file_path_1 = tmp_path / "new-file1.txt"
    mock_file_path_2 = tmp_path / "new-file2.txt"
    mock_file_path_1.touch()
    mock_file_path_2.touch()
    mock_file_path_1.write_text("Hello")
    mock_file_path_2.write_text("My name is Alex")
    context = {"all_files": [str(mock_file_path_1), str(mock_file_path_2)]}

    with patch(
        "pro_filer.cli_helpers._get_printable_file_path",
        mock__get_printable_file_path,
    ):
        show_disk_usage(context)

    captured = capsys.readouterr()
    output = captured.out

    assert "15 (75%)" in output

    assert "5 (25%)" in output

    assert "Total size: 20\n" in output


def test_show_disk_usage_with_empty_files(capsys):
    context = {"all_files": []}

    show_disk_usage(context)
    captured = capsys.readouterr()
    output = captured.out
    assert output == "Total size: 0\n"


def test_show_disk_usage_correctly_order(tmp_path, capsys):
    mock__get_printable_file_path = Mock()
    mock_file_path_1 = tmp_path / "new-file1.txt"
    mock_file_path_2 = tmp_path / "new-file2.txt"
    mock_file_path_1.touch()
    mock_file_path_2.touch()
    mock_file_path_1.write_text("Hello")
    mock_file_path_2.write_text("My name is Alex")
    context = {"all_files": [str(mock_file_path_1), str(mock_file_path_2)]}

    with patch(
        "pro_filer.cli_helpers._get_printable_file_path",
        mock__get_printable_file_path,
    ):
        show_disk_usage(context)

    captured = capsys.readouterr()
    output = captured.out

    file1_index = output.index("new-file1.txt")
    file2_index = output.index("new-file2.txt")

    assert file1_index > file2_index
