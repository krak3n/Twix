#
# python.install
#
# Install python 3.3 and python-dev 3.3 packages
#

.python3.3:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa

.python3.3-dev:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa
