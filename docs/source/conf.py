# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#import os
import sys
from pathlib import Path
#sys.path.insert(0, os.path.abspath('./episol/'))
sys.path.insert(0,str(Path('../../','episol').resolve()))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Epipy Documentation'
copyright = '2025, pswanson'
author = 'pswanson'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'nbsphinx',
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx.ext.intersphinx',
        "sphinx.ext.viewcode",
        "sphinx_gallery.load_style",
        "sphinx.ext.githubpages",
    ]

templates_path = ['_templates']
exclude_patterns = []


autodoc_typehints = "description"
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_static_path = ['_static']

html_logo = '_static/out_4.png'

