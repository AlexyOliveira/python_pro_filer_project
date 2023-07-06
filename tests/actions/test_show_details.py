from pro_filer.actions.main_actions import show_details  # NOQA


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
    assert output == (
        "File name: new-file.txt\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .txt\n"
        "Last modified date: 2023-07-05\n"
    )


def test_if_file_with_no_extension(capsys, tmp_path):
    mock_file_path = tmp_path / "new-file"
    mock_file_path.touch()
    no_extension_context = {"base_path": str(mock_file_path)}

    show_details(no_extension_context)

    captured = capsys.readouterr()

    output = captured.out
    assert output == (
        "File name: new-file\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-07-05\n"
    )
