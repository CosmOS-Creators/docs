# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess
from sphinx.application import Sphinx
sys.path.insert(0, os.path.abspath("."))
from doxy_group_collector import convert_doxygen_to_rst, convert_doxygen_to_rst_list

sys.path.insert(0, os.path.abspath("../customBox/python"))


# -- Project information -----------------------------------------------------

project = "CosmOS"
copyright = "2021, Pavol Kostolansky, Florian Laschober"
author = "Pavol Kostolansky, Florian Laschober"

# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "breathe",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    'sphinx_toolbox.collapse',
    'sphinx_panels',
]

breathe_projects = {
    "CosmOS": "doxyout/xml"
}

breathe_default_project = "CosmOS"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

html_logo = "images/cosmos/cosmosWhite.png"
html_theme_options = {
    "sidebar_hide_name": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

html_static_path = ['_static', 'whitepaper']

html_favicon = 'favicon.ico'



def setup(app: Sphinx) -> None:
    MODULE_GLOB = "group__*__module.xml"
    DOXYFILE_NAME = "cosmos/docs/Doxyfile"
    GENERATED_OUTPUT_FOLDER = "doxygen_rst"

    # set recursice to false for a significant generation time reduction
    doxygen_command = ["doxygen", DOXYFILE_NAME]
    returncode = subprocess.call(doxygen_command, shell=True, cwd="../../")
    if(returncode == 0):
        convert_doxygen_to_rst(
            breathe_projects[breathe_default_project],
            GENERATED_OUTPUT_FOLDER,
            "Core Modules",
            "core_modules",
            MODULE_GLOB,
            breathe_default_project,
            recursive = True,
            max_nesting_level = 2,
            exclude_groups=["CIL_module"]
        )
        convert_doxygen_to_rst_list(
            breathe_projects[breathe_default_project],
            GENERATED_OUTPUT_FOLDER,
            "Integration Modules",
            "integration_modules",
            ["CIL_module"],
            breathe_default_project,
            recursive = True,
            max_nesting_level = 2
        )
    else:
        exit()
