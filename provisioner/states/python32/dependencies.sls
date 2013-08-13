#
# python32.dependencies
#
# Python 3.2 installation dependencies
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
