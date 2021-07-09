# -*- coding: utf-8 -*-
#
# Kolibri Studio documentation build configuration file, created by
# sphinx-quickstart on Mon Oct 16 16:46:14 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime

from sphinx.builders.html import StandaloneHTMLBuilder


# -- Project information -----------------------------------------------------

project = u'Kolibri Studio'
copyright = u"{year:d}, Learning Equality".format(year=datetime.now().year)
author = u'Learning Equality'


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.todo",
    "sphinx_rtd_theme",
    "notfound.extension",
]

linkcheck_ignore = [
    "http://diagramcenter.org/making-images-accessible.html",
    "https://www.w3.org/TR/html5/semantics-embedded-content.html#alt-text",
    "https://www.3playmedia.com/2016/06/16/closed-captioning-subtitling-standards-in-ip-video-programming/",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u'0.2.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'default'
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    os.system("sphinx-apidoc --doc-project='Python Reference' -f -o . ../kolibri ../kolibri/test ../kolibri/deployment/ ../kolibri/dist/")

# Trying out Divio theme https://github.com/divio/divio-docs-theme/

#if not on_rtd:  # only import and set the theme if we're building docs locally
#    import divio_docs_theme
#    html_theme = 'divio_docs_theme'
#    html_theme_path = ['.', divio_docs_theme.get_html_theme_path()]
#    html_theme_options = {
#        'display_version': False,
#        'prev_next_buttons_location': 'both',
#        'style_external_links': True,
#        'show_cloud_banner': False,
    #        'cloud_banner_markup': """
    #            <div class="divio-cloud">
    #                <span class="divio-cloud-caption">Cloud deployment by Divio</span>
    #                <iframe src="https://player.vimeo.com/video/435660924" width="226" height="141" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    #                <p>There's a better, faster, easier way to develop, deploy and manage web applications.</p>
    #                <a class="btn-neutral divio-cloud-btn" target="_blank" href="https://www.divio.com">Find out more at Divio</a>
    #            </div>
    #        """,
#    }


if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = ['.', sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Kolibri Studio User Guide"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ["extras"]

# Approach for custom stylesheet:
# adapted from: http://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
# and https://github.com/altair-viz/altair/pull/418/files
# https://github.com/rtfd/sphinx_rtd_theme/issues/117
def setup(app):
    # Add our custom CSS overrides
    app.add_stylesheet('theme_overrides.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'KolibriStudiodoc'

rst_prolog = """
.. role:: raw-html(raw)
      :format: html

.. |br| replace:: :raw-html:`<br /><br />`


"""

with open("./rstIconReplacements.txt") as f:
    replacements = f.read()
    rst_prolog += "\n" + replacements


# Apr 5th: directive to allow .gif use for HTML docs with .png fallback for latexpdf
StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml",
    "image/gif",
    "image/png",
    "image/jpeg",
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'kolibristudio', u'Kolibri Studio Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'KolibriStudio', u'Kolibri Studio Documentation',
     author, 'KolibriStudio', 'One line description of project.',
     'Miscellaneous'),
]




# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    "fncychap": "\\usepackage{fncychap}",
    "fontpkg": "\\usepackage[default]{lato}\\usepackage[T1]{fontenc}",
    "figure_align": "htbp",
    # The font size ('10pt', '11pt' or '12pt').
    #
    "pointsize": "12pt",
    "extraclassoptions": "oneside",
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    "preamble": r"""
        %%% FRONTMATTER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}
        %\usepackage{amsmath,amsfonts,amssymb,amsthm}   % not needed since we don't math
        %\usepackage{graphicx}                          % not needed here because imported in sphinx.sty
        %
        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        % \usepackage{color}                            % not needed here because imported in sphinx.sty
        % \usepackage{transparent}
        % \usepackage{eso-pic}
        % \usepackage{lipsum}

        %% spacing between line
        \usepackage{setspace}
        \onehalfspacing
        % \doublespacing
        % \singlespacing

        %%% datetime
        \usepackage{datetime}
        \newdateformat{MonthYearFormat}{\monthname[\THEMONTH], \THEYEAR}



        %%% HEADERS TEXT %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \usepackage{fancyhdr}
        % plain = first-page of each chapter
        \fancypagestyle{plain}{
            \fancyhf{}
            \fancyhead{}
            \renewcommand{\headrulewidth}{0pt}
            \renewcommand{\footrulewidth}{0pt}
            \fancyfoot[C]{{\small\thepage}}
        }
        % normal = subclass of plain = applies to rest of pages
        \fancypagestyle{normal}{
            \fancyhead{}
            \fancyhead[L]{\small\rightmark}
            \fancyhead[R]{{\small\thepage}}
            \renewcommand{\headrulewidth}{0.4pt}
            \renewcommand{\footrulewidth}{0pt}
            \fancyfoot[C]{{}}  % undo the \fancyfoot[C]{{\small\thepage}} in the base class
            %   \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Learning Equality} }{\href{https://learningequality.org}{\tiny learningequality.org}}}
            %%% Alternating Footer for two side
            %%% \fancyfoot[RO, RE]{\scriptsize Learning Equality (info@learningequality.org)}
        }
        %% callback that changes document header text
        %%                                               = section number counter (\thesection)
        %%                                                          + the section title
        \renewcommand{\sectionmark}[1]{\markboth{}{\emph{\thesection~#1}}}
        %%%% optional: uncomment next line to change header on every \section and not on \subsection
        %%%% \renewcommand{\subsectionmark}[1]{}


        %%reduce spacing for itemize ???
        \usepackage{enumitem}
        \setlist{nosep}

        %%%%%%%%%%% Quote Styles at the top of chapter ???
        \usepackage{epigraph}
        \setlength{\epigraphwidth}{0.8\columnwidth}
        \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%%%%%%%%%% Quote for all places except Chapter
        \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}

    """,
    "maketitle": r"""

        %%% SET PDF INFO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % Note: this has to be after preamble where \title and \author are defined
        \makeatletter
        \hypersetup{
            pdftitle=\@title,
            pdfauthor=\@author,
            pdfkeywords={Kolibri, Kolibri Studio, offline learning, open educational resources},
            pdfsubject={Kolibri},
            pdfstartview=Fit,   % default value
            pdfstartpage=1,     % default value
            % other available options:
            % pdfstartview={FitH},
            % pdfpagelayout=SinglePage,
            % pdfpagelabels=true,
            % bookmarksopen=true,
            % bookmarksopenlevel=0
        }
        \makeatother

        %%%  COVER PAGE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering
            \vspace*{20mm} %%% * is used to give space from top

            \begin{figure}[!h]
            \centering
            \includegraphics[width=0.95\textwidth]{kolibri-contexts.pdf}
            \end{figure}

            \vspace{0mm}
            \textbf{\Huge {Kolibri Studio User Guide}}

            \vspace{0mm}
            \small Published by Learning Equality

            %% \vfill adds at the bottom
            \vfill
            \small \textit{More information available at }{\href{https://learningequality.org}{learningequality.org}}
        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        % \listoffigures
        % \listoftables
        \clearpage
        \pagenumbering{arabic}
        """,
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
    #
    # GLOBAL OPTIONS FOR THE sphynx.sty STYLE CLASS ############################
    "sphinxsetup": r"""
        hmargin={1in,1in}, vmargin={1.2in,0.7in}, \
        TitleColor={rgb}{0,0,0}, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}, \
        verbatimwithframe=false, \
        VerbatimColor={rgb}{0.95,0.95,0.95}, \
        verbatimvisiblespace={}, \
        verbatimcontinued={}""",
    "tableofcontents": " ",
}


# Show URLs in footnote
latex_show_urls = "footnote"

# Grouping the document tree into LaTeX files. List of tuples:
latex_documents = [
    (
        "index",  # source start file,
        "kolibri.tex",  # target name,
        u"Kolibri Studio User Guide",  # title,
        u"Published by learningequality.org",  # author,
        "manual",  # documentclass [howto, manual, or own class])
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None
latex_logo = "kolibri-contexts.pdf"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True
