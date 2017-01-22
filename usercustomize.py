import os
import sys
import site
import contextlib

# Try to copy what https://github.com/python/cpython/blob/master/Lib/site.py#L425
# is doing.

venv_loc = os.path.join(os.getcwd(), 'python_modules')
with contextlib.suppress(FileNotFoundError):
    with open(os.path.join(venv_loc, 'pyvenv.cfg'), encoding='utf-8') as file:
        for line in file:
            if '=' in line:
                key, _, value = line.partition('=')
                key = key.strip().lower()
                value = value.strip()
                if key == 'include-system-site-packages':
                    include_system_site = True if value == 'true' else False
                elif key == 'home':
                    sys_home = value

    # Build new site path
    site_packages = site.getsitepackages([venv_loc,])
    if include_system_site:
        for loc in sys.path:
            if loc.endswith('site-packages'):
                site_packages.append(loc)
    # Remove old site packages
    for path in sys.path[::-1]:
        if path.endswith('site-packages'):
            sys.path.remove(path)
    # Add new site packages
    sys.path.extend(site_packages)

    # Setup other sys vars
    sys._home = sys_home
    sys.prefix = sys.exec_prefix = venv_loc
    sys.executable = os.path.join(venv_loc, 'bin', 'python')
