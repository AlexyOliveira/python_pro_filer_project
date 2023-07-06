from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_files_and_directories(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src",
            "src/utils",
            "src",
            "src/utils",
        ],
    }
    show_preview(context)

    captured = capsys.readouterr()

    output = captured.out

    expected_output = (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', 'src/__init__.py', 'src/app.py']\n"
        "First 5 directories: ['src', 'src/utils', 'src', "
        "'src/utils', 'src']\n"
    )

    assert output == expected_output


def test_show_preview_with_no_files_and_directories(capsys):
    context = {
        "all_files": [],
        "all_dirs": [],
    }
    expected_output = "Found 0 files and 0 directories\n"
    show_preview(context)

    captured = capsys.readouterr()

    output = captured.out

    assert output == expected_output
