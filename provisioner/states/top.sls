#
# Top SLS File
#

base:
  '*':
    # Standard
    - curl
    - tree
    - wget
    - git
    # Python Related
    - python
    - python26
    - python27
    - python32
    - python33
    - setuptools
    - pip
    - virtualenv
    # Project states, create virtualenvs, db etc
    - project
    # Local states, located at /vagrant/.salt and at ~/.salt on the Host
    - local
