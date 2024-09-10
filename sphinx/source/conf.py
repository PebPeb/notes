# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify
import os


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
# Sphinx Implimentation
# ============================================================================

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes'
copyright = '2023, Bryce Keen'
author = 'Bryce Keen'

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