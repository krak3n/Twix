#
# pip.install
#
# Install PIP
#

.pip:
  cmd:
    - run
    - name: 'curl -L https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python'
    - unless: 'test -f /usr/local/bin/pip'
    - require:
      - pkg: curl.install::curl
      - pkg: python.install::python
      - pkg: python.install::python-dev
      - cmd: setuptools.install::setuptools
