import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo'
]

todo_include_todos = True

templates_path = ['ytemplates']
source_suffix = '.rst'
master_doc = 'index'

project = u'ONELVXE Material Pipeline'
copyright = u'2016, lvxejay'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = ['includes/*']

pygments_style = 'sphinx'

htmlhelp_basename = 'ONELVXEMaterialPipelinedoc'

latex_elements = {}
latex_documents = [
  ('index', 'ONELVXEMaterialPipeline.tex', u'ONELVXE Material Pipeline Manual',
   u'lvxejay', 'manual'),
]

man_pages = [
    ('index', 'ONELVXEMaterialPipeline', u'ONELVXE Material Pipeline Manual',
     [u'lvxejay'], 1)
]
texinfo_documents = [
  ('index', 'ONELVXEMaterialPipeline', u'ONELVXE Material Pipeline Manual',
   u'lvxejay', 'ONELVXEMaterialPipeline', 'ONELVXE Material Pipeline',
   'Miscellaneous'),
]

epub_title = u'ONELVXE Material Pipeline'
epub_author = u'lvxejay'
epub_publisher = u'lvxejay'
epub_copyright = u'2016, lvxejay'
epub_exclude_files = ['search.html']
