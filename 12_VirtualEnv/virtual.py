# A virtual environment (virtualenv or venv) is an isolated Python environment where you can install packages for one project without affecting other projects or the system-wide Python installation.

# Think of it like this:

# Imagine you have three projects.

# Project A
# Project B
# Project C

# Project A needs:
# Django 4.2

# Project B needs:
# Django 5.2

# If you install Django globally, you'll have a 
# conflict because only one version can be active at a time.

# A virtual environment solves this.

# Computer
# │
# ├── Project A
# │      ├── Virtual Environment
# │      │      └── Django 4.2
# │
# ├── Project B
# │      ├── Virtual Environment
# │      │      └── Django 5.2
# │
# └── Project C
#        ├── Virtual Environment
#               └── Flask

# Each project has its own packages.