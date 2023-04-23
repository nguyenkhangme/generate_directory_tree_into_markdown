import numpy as np
import os


def generate_directory_tree_into_markdown(startpath):
    except_folders=['image', 'stylesheets', 'font', 'javascripts', '.ipynb_checkpoints']
    accept_files = ['.md']
    markdown_content=''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        if not np.array([x in root for x in except_folders]).any():
            markdown_content += f'{indent}- [{os.path.basename(root)}](<{root}>)/\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if np.array([x in f for x in accept_files]).any():
                markdown_content += f'{subindent}- [{f}](<{root}/{f}>)\n'
    return markdown_content


if __name__ == "__main__":
    file_path = './tocs.md'
    with open(file_path,'w') as fp:
        fp.write('# Table of Contents\n\n')
        fp.write(generate_directory_tree_into_markdown('docs'))
