#
# setuptools.install
#
# Install python setuptools
#

.setuptools:
  cmd:
    - run
    - name: 'curl -L https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python'
    - unless: 'python -c "import setuptools"'
    - require:
      - pkg: curl.install::curl
      - pkg: python.install::python
      - pkg: python.install::python-dev
