#
# python.install
#
# Install python 2.7 and python-dev 2.7 packages
#

.python2.7:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa

.python2.7-dev:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa

