#
# python.install
#
# Install python 3.2 and python-dev 3.2 packages
#

.python3.2:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa

.python3.2-dev:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa
