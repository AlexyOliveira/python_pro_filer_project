""" Arquivo que estudantes devem editar  """


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=lambda x: x.count("/"))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []
    search_term = search_term.lower() if not case_sensitive else search_term

    for path in context["all_files"]:
        file_name = (
            path.split("/")[-1].lower()
            if not case_sensitive
            else path.split("/")[-1]
        )

        if search_term in file_name:
            found_files.append(path)

    return found_files
