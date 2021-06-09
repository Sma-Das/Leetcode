import os


if __name__ == '__main__':
    file_name = "README.md"

    terms = [
        "### 1-Easy\n",
        "### 2-Medium\n",
        "### 3-Hard\n",
    ]

    ignore_list = [
        "LinkedListBuilder.py",
        "__pycache__"
    ]

    with open(file_name, "r+") as file:
        contents = file.readlines()
        for term in terms:
            if term not in contents:
                raise IndexError(f"Term not found: {term}")
            i = contents.index(term)
            folder_name = term.split()[1].strip()
            folder_contents = os.listdir(f"./{folder_name}")

            for j, project in enumerate(folder_contents, start=1):
                if (proj_name := f"> * {project}\n") in contents or project in ignore_list:
                    continue
                else:
                    contents.insert(i+j, proj_name)
    with open(file_name, "w") as file:
        file.write("".join(contents))
    print(f"Updated {file_name}")
