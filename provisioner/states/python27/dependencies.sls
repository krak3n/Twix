#
# python27.dependencies
#
# Python 2.7 installation dependencies
#

.python-software-properties:
  pkg:
    - installed

.versions_ppa:
  pkgrepo:
    - managed
    - ppa: fkrull/deadsnakes
    - require:
      - pkg: .python-software-properties
