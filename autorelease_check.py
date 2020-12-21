#/usr/bin/env python
from __future__ import print_function
import setup
import contact_map
from autorelease import DefaultCheckRunner, conda_recipe_version
from autorelease.version import get_setup_version
from packaging.version import Version

repo_path = '.'
SETUP_VERSION = get_setup_version(None, directory='.')
versions = {
    'package': contact_map.version.version,
    'setup.py': SETUP_VERSION,
    'conda-recipe': conda_recipe_version('ci/conda-recipe/meta.yaml'),
}

RELEASE_BRANCHES = ['stable']
RELEASE_TAG = "v" + Version(SETUP_VERSION).base_version

if __name__ == "__main__":
    checker = DefaultCheckRunner(
        versions=versions,
        setup=setup,
        repo_path='.'
    )
    checker.release_branches = RELEASE_BRANCHES + [RELEASE_TAG]

    tests = checker.select_tests()
    n_fails = checker.run_as_test(tests)
