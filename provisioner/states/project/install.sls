#
# project.install
#
# Installs the project
#

.setup:
  cmd:
    - run
    - name: /home/vagrant/.virtualenvs/twix/bin/pip install -e .[develop]
    - cwd: /home/vagrant/twix
    - user: vagrant
    - shell: /bin/bash
    - require:
      - virtualenv: .virtualenv::exists
