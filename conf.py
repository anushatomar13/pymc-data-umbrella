# Sphinx configuration build
# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_thebe",
    "sphinxcontrib.youtube"
]

thebe_config = {
   "selector": "div.highlight-ipython3"
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# MyST related params
jupyter_execute_notebooks = "auto"
execution_excludepatterns = ["*.ipynb"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "substitution"
]
myst_substitutions = {
  "meenal": "Meenal Jhajharia"
}

# use numbered figures
numfig = True

# The base toctree document.
master_doc = "index"

# General information about the project.
project = "PyMC-Data Umbrella Sprint"
copyright = "2021, Sprint contributors"
author = "Sprint Contributors"
pymc_url = "https://docs.pymc.io/en/latest/"

version = "0.1"
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints", "README.md", "CONTRIBUTING.md", "jupyter_execute"
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "external_links": [
    {
        "name": "PyMC", "url": pymc_url
    },
    {
        "name": "Data Umbrella", "url": "https://www.dataumbrella.org"
    },
    ],
    "show_toc_level": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pymc-devs/pymc-data-umbrella",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.pymc.io",
            "icon": "fab fa-discourse",
        }
    ],
    "use_edit_page_button": True,
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["search-field.html", "navbar-icon-links.html"],
    "search_bar_text": "Search...",
    "footer_items": ["coc_notice", "copyright", "sphinx-version"],
    "google_analytics_id": "G-8YL5S5CGYD",
}

html_context = {
    "github_user": "pymc-devs",
    "github_repo": "pymc-data-umbrella",
    "github_version": "main",
    "doc_path": ".",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]

# -- Options for HTMLHelp output ------------------------------------------

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logo.png"


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Example configuration for intersphinx
intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pymc": (pymc_url, None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

thebe_config = {
    "always_load": True,
    "repository_url": "https://github.com/pymc-devs/pymc-sandbox",
    "repository_branch": "sprint"
}