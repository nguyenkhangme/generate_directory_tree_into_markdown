# generate_directory_tree_into_markdown

Use for documentation websites, this repo provides a Python script and demonstrates how to use GitHub Actions to automate the generation of a TOC for the repository everytime new push to main happens. The TOCs generator allow user to select specific file name patterns and exclude folder names

---

Using Python to generate a directory tree into markdown. This is helpful for document pages with accepted files (like .md) and except folders (like images) to generate

Change `except_folders` and `accept_files` inside `generate_directory_tree_into_markdown`

The fancy version: generate_directory_tree_into_markdown.py, use it with requirements.txt

The build faster version (using for this repository): generate_directory_tree_into_markdown_without_numpy.py

Future improvement: add `where_to_place_markdown_file`  to `generate_directory_tree_into_markdown`
