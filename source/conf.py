# -*- coding: utf-8 -*-
#
# Supporting Python 3 documentation build configuration file, created by
# sphinx-quickstart on Tue Dec 15 13:40:39 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration ----------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'UTF-8'

# The master toctree document.
master_doc = 'bookindex'

# General information about the project.
project = u'Supporting Python 3'
copyright = u'2011-2015, Lennart Regebro'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0-dev'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'none'
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

#rst_prolog = "\n.. include:: /%s/source/intro.rst\n\n"%(os.path.abspath('.'),)

# -- Options for HTML output ----------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'agogo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'footerbg': '#FFCC33',
                      'headerbg': '#FFCC33',
                      'documentwidth': '40em',
                      'pagewidth': '60em',
                      }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = u'Supporting Python 3 - The Book Site'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'SupportingPython3'

html_show_sphinx = False

# -- Options for LaTeX output ----------

# The paper size ('letter' or 'a4').
#latex_paper_size = '{6in,9in}'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '11pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('bookindex', 'SupportingPython3.tex', u'Supporting Python 3',
   u'Lennart Regebro', 'sphinxcustom'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
print_form = r"hdivide={0.75in,*,0.75in},vdivide={1in,*,1in},papersize={6in,9in}"
screen_form = r"hdivide={1in,*,1in},vdivide={1in,*,1in},papersize={8.27in,11in}"
tablets_form = r"hdivide={0.1in,*,0.1in},vdivide={0.7in,*,0.7in},papersize={7in,9in}"
phones_form = r"hdivide={0.1in,*,0.1in},vdivide={0.7in,*,0.7in},papersize={4.8in,7.2in}"

print_latex_elements = {
    'preamble': r"""
\usepackage[dvips]{geometry}
\geometry{bindingoffset=0in,""" + print_form + r"""}
\authoraddress{Ulica Retoryka 15/5\\*31-108 Krak\'{o}w\\*Poland\\*e-mail: info@colliberty.com}
\usepackage{fontspec}
\usepackage{wasysym}
\usepackage[titles]{tocloft}

\hyphenpenalty=1500
\widowpenalty=10000
\clubpenalty=10000

%% Font changes:
%% Yes, use bold for regular:
\setsansfont[
    Path=/home/lregebro/.fonts/,
    Extension=.TTF,
    UprightFont= *B___,
    BoldFont=*B___,
    ItalicFont=*I___,
    BoldItalicFont=*BI__,
    Mapping=tex-text
]{FLUX}
\setmonofont[Scale=0.85]{DejaVu Sans Mono}
\setmainfont[
    Extension=.otf,
    UprightFont= *-regular,
    BoldFont=*-bold,
    ItalicFont=*-italic,
    BoldItalicFont=*-bolditalic,
    Mapping=tex-text
]{texgyreschola}
%%\setmainfont{TeX Gyre Schola}
\setlength{\headheight}{14pt}
\renewcommand{\cftchapfont}{%
  \Large\sffamily
}
\renewcommand{\cftchappagefont}{%
  \Large\sffamily
}
\renewcommand{\cftsecfont}{%
  \large\sffamily
}
\renewcommand{\cftsecpagefont}{%
  \large\sffamily
}
\renewcommand{\textgreater}{>}

%% Get rid of link colors
\definecolor{TitleColor}{rgb}{0,0,0}
\definecolor{InnerLinkColor}{rgb}{0,0,0}
\definecolor{OuterLinkColor}{rgb}{0,0,0}

%% Unicode character redefinitions
\catcode`^^^^00a0=\active
\def^^^^00a0{\nobreakspace}
\catcode`^^^^00f6=\active
\def^^^^00f6{\"{o}}
\catcode`^^^^00dc=\active
\def^^^^00dc{\"{U}}
\catcode`^^^^00c4=\active
\def^^^^00c4{\"{A}}
\catcode`^^^^00e6=\active
\def^^^^00e6{\ae}
\catcode`^^^^00d6=\active
\def^^^^00d6{\"{O}}
\catcode`^^^^00e9=\active
\def^^^^00e9{\'{e}}

%% Unicode character redefinitions to checkboxes
\catcode`^^^^2610=\active
\def^^^^2610{\leavevmode\hbox{\wasyfamily\char50\hss}}
\catcode`^^^^2611=\active
\def^^^^2611{\ensuremath{\CheckedBox}}
""",
    'releasename': 'Revision',
    'pointsize': '11pt',
}


latex_elements = print_latex_elements

# Documents to append as an appendix to all manuals.
latex_appendices = ['differences', 'stdlib']

# If false, no module index is generated.
latex_use_modindex = True

latex_show_pagerefs = True

# PDFBuilder stuff

pdf_documents = [
  ('bookindex', 'SupportingPython3.pdf', u'Supporting Python 3', u'Lennart Regebro'),
]

pdf_stylesheets = ['sphinx','kerning','a4']

pdf_appendices = ['differences', 'stdlib']
