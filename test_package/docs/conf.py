# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# SunPy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for sunpy or sunpy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_docs" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import os
import sys
import pathlib
import datetime
from distutils.version import LooseVersion


# -- Import Base config from sphinx-astropy ------------------------------------
try:
    from sphinx_astropy.conf.v1 import *
except ImportError:
    print('ERROR: the documentation requires the "sphinx-astropy" package to be installed')
    sys.exit(1)

try:
    import sphinx_gallery
    from sphinx_gallery.sorting import ExplicitOrder
except ImportError:
    print('ERROR: the documentation requires the "sphinx-gallery" package to be installed')
    sys.exit(1)

from pkg_resources import get_distribution
versionmod = get_distribution('test_package')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# The short X.Y version.
version = '.'.join(versionmod.version.split('.')[:3])
# The full version, including alpha/beta/rc tags.
release = versionmod.version.split('+')[0]
# Is this version a development release
is_development = '.dev' in release

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.6'

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("x.y.z")` here.
check_sphinx_version(needs_sphinx)

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog = """
.. SunPy
.. _SunPy: https://sunpy.org
.. _`SunPy mailing list`: https://groups.google.com/group/sunpy
.. _`SunPy dev mailing list`: https://groups.google.com/group/sunpy-dev
"""

# -- Project information ------------------------------------------------------
project = 'test_package'
author = 'The SunPy Community'
copyright = '{}, {}'.format(datetime.datetime.now().year, author)

try:
    from sunpy_sphinx_theme.conf import *
except ImportError:
    print('ERROR: the documentation requires the "sunpy_sphinx_theme" package to be installed')
    sys.exit(1)

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f'{project} v{release}'

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# -- Options for LaTeX output --------------------------------------------------
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + ' Documentation', author, 'manual')]

# -- Options for manual page output --------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + ' Documentation', [author], 1)]

# -- Swap to Napoleon ---------------------------------------------------------
# Remove numpydoc
extensions.remove('numpydoc')
extensions.append('sphinx.ext.napoleon')

# Disable having a separate return type row
napoleon_use_rtype = False
# Disable google style docstrings
napoleon_google_docstring = False


# -- Options for the Sphinx gallery -------------------------------------------
extensions += ["sphinx_gallery.gen_gallery"]
path = pathlib.Path.cwd()
example_dir = path.parent.joinpath('examples')
sphinx_gallery_conf = {
	'backreferences_dir': path.joinpath('generated', 'modules'),  # path to store the module using example template
	'filename_pattern': '^((?!skip_).)*$',  # execute all examples except those that start with "skip_"
	'examples_dirs': example_dir,  # path to the examples scripts
	'subsection_order': ExplicitOrder([(os.path.join('..', 'examples/'))]),
	'gallery_dirs': path.joinpath('generated', 'gallery'),  # path to save gallery generated examples
	'abort_on_example_error': False,
	'plot_gallery': True
}
