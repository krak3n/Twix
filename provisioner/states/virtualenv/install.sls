#
# virtualenv.install
#
# Install virtualenv and virtualenvwrapper.
#

.virtualenv:
  pip:
    - installed
    - require:
      - cmd: pip.install::pip

.virtualenvwrapper:
  pip:
    - installed
    - require:
      - pip: .virtualenv
