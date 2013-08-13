#
# python.install
#
# Install python 2.6 and python-dev 2.6 packages
#

.python2.6:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa

.python2.6-dev:
  pkg:
    - installed
    - require:
      - pkgrepo: .dependencies::versions_ppa
