#
# project.virtualenv
#
# Create a project python virtual environment
#

.exists:
  virtualenv:
    - managed
    - name: /home/vagrant/.virtualenvs/twix
    - runas: vagrant
    - no_site_packages: False
    - require:
      - pip: virtualenv.install::virtualenv
