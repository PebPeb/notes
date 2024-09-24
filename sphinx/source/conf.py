# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme
import recommonmark
import os
from jinja2 import Environment, FileSystemLoader
from recommonmark.transform import AutoStructify
import re


target_dir = './../../notes'
symlink_path = './notes'

try:
    # Create a symbolic link
    os.symlink(target_dir, symlink_path)
    print(f"Symbolic link created from {symlink_path} to {target_dir}")
except FileExistsError:
    print(f"Error: The symbolic link already exists at {symlink_path}")
except FileNotFoundError:
    print(f"Error: The target directory does not exist at {target_dir}")
except PermissionError:
    print(f"Error: Permission denied while creating the symbolic link")
except OSError as e:
    print(f"Error: {e}")


# ============================================================================
# Building Index File
# ============================================================================

project_name = "My Notes"  # Replace with your project's name
source_dir = './notes'       
template_file = 'index.rst.tmpl'
output_file = './index.rst'

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(template_file)

def extractChapterFiles(file_path):
    extracted_files = []
    with open(file_path, 'r') as file:
        lines = file.readlines()    
        in_toc = False
        
        for line in lines:
            # Check for the start of the toctree
            if '.. toctree::' in line:
                in_toc = True
                continue

            # Extract filenames from the toctree
            if in_toc:
                # Using regex to find markdown files
                match = re.match(r'^\s*([^\s]+\.md|[^\s]+\.rst)', line)
                if match:
                    extracted_files.append(os.path.dirname(file_path) + '/' + match.group(1))
    return extracted_files

def find_files(directory):
    extracted_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.rst')) and file.lower() == 'chapter.rst':
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                extracted_files.extend(extractChapterFiles(source_dir + '/' + relative_path))
                yield relative_path.replace('\\', '/')
        
        for file in files:
            if file.endswith(('.rst', '.md')) and file != 'index.rst' and file.lower() != 'chapter.rst':
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                # print(relative_path)
                if (source_dir + '/' + relative_path) not in extracted_files:
                # Replace backslashes with forward slashes for Sphinx compatibility
                    yield relative_path.replace('\\', '/')

files = sorted(find_files(source_dir))

# Render the template with context
rendered_content = template.render(project_name=project_name, files=files)

# Write the rendered content to index.rst
with open(output_file, 'w') as f:
    f.write(rendered_content)

print(f"Generated {output_file} successfully.")

# ============================================================================
# Sphinx Implimentation
# ============================================================================

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes'
copyright = '2023, Bryce Keen'
author = 'Bryce Keen'

latex_engine = 'xelatex'  # or 'lualatex'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    'recommonmark',
    'sphinx_markdown_tables',
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []

# Auto-structure Markdown files
def setup(app):
    app.add_transform(AutoStructify)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Set the theme.
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]