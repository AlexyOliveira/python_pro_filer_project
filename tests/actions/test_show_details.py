from pro_filer.actions.main_actions import show_details  # NOQA
import datetime


def test_if_file_does_not_exist(capsys):
    not_exist_context = {"base_path": "/home/trybe/????"}

    show_details(not_exist_context)

    captured = capsys.readouterr()

    output = captured.out

    assert output == "File '????' does not exist\n"


def test_if_file_exist(capsys, tmp_path):
    mock_file_path = tmp_path / "new-file.txt"
    mock_file_path.touch()
    exist_context = {"base_path": str(mock_file_path)}

    show_details(exist_context)

    captured = capsys.readouterr()

    output = captured.out
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    expected_output = (
        f"File name: new-file.txt\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: .txt\n"
        f"Last modified date: {current_date}\n"
    )
    assert output == expected_output


def test_if_file_with_no_extension(capsys, tmp_path):
    mock_file_path = tmp_path / "new-file"
    mock_file_path.touch()
    no_extension_context = {"base_path": str(mock_file_path)}

    show_details(no_extension_context)

    captured = capsys.readouterr()

    output = captured.out
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    assert output == (
        f"File name: new-file\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {current_date}\n"
    )
