#
# Sphinx Documentation Config
#

import os
import sys

from datetime import datetime

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import twix

now = datetime.now()

project = u'Twix'
copyright = u'{0}, Christopher Reeves'.format(now.year)

version = '{0}.{1}'.format(*twix.__VERSION__[:2])
release = twix.get_version()

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

# Theme
sys.path.append(os.path.abspath('_themes'))
html_static_path = ['_static']
html_theme_path = ['_themes']
html_theme = 'flask'
html_theme_options = {
    'index_logo': 'twix.jpeg'
}

man_pages = [
    ('index', 'Twix', u'Twix Documentation',
     [u'Christopher Reeves'], 1)
]

texinfo_documents = [
    ('index', 'Twix', u'Twix Documentation',
     u'Christopher Reeves', 'Twix', 'Project scaffolding from custom '
     'templates.', 'Miscellaneous'),
]
