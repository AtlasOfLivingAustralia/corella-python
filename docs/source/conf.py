# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import corella

project = 'corella'
copyright = 'Atlas of Living Australia'
author = 'Atlas of Living Australia'

# add path for corella
sys.path.insert(0,"../../corella/src/corella/")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinx-prompt',
              'sphinxcontrib.programoutput',
              'sphinx_design',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosectionlabel']

autosectionlabel_prefix_document = True
napoleon_use_param = True
myst_enable_extensions = ["colon_fence"]

version = str(corella.__version__)
release = version
source_path = os.path.dirname(os.path.abspath(__file__))

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
        "navbar_align": "content",
        "github_url": "https://github.com/AtlasOfLivingAustralia/corella-python",
        "secondary_sidebar_items": ["page-toc"],
        "logo": {
                "image_light": "_static/logo/logo.png", # didn't have dir before
                "image_dark": "_static/logo/logo.png",
        },
}

# was image_light
html_sidebars = {
        "index": [],
        "search": [],
    "**": ["sidebar-nav-bs"]
}

html_static_path = ['_static']

html_logo = "_static/logo/logo.png"

html_favicon = '_static/logo/favicon.ico'

html_css_files = ['css/extra.css']

html_style = 'css/extra.css'