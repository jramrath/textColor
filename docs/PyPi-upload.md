# Uploading to PyPi

More info [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

Remove all old distribution files in 'dist/'

Make sure you have the latest version of 'build':

> python3 -m pip install --upgrade build

In the same directory as 'pyproject.toml':

> python3 -m build

Now that the distribution files have been generated, make sure twine is up to date:

> python3 -m pip install --upgrade twine

Again, in the same directory as 'pyproject.toml':

> python3 -m twine upload dist/*
>
> username: \_\_token__
>
> password: \<API token from pypi>
