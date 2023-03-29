# LabVIEW-Utils Package

## Quick Start
### Install
```console
pip install git+ssh://git@github.com/htllc/labview-utils.git
```

### Usage
<p align="center">
    <img src="https://user-images.githubusercontent.com/7851827/228423618-214d9fc4-4b1a-4c2e-9afd-6e27e5c95487.png">
    <br><br>
    <img src="https://user-images.githubusercontent.com/7851827/228423664-3f065cd6-cff8-440e-a00e-0113a8fdf367.png">
</p>

TODO: add a helper LabVIEW VI to the repos to encapsulate the intended use of `get_module_path()` as illustrated above.

Of course, the point is to use it from LabVIEW, but here's a python demo:
```python
>>> from labview_utils import get_module_path
>>> get_module_path('collections.abc')
'C:\\Program Files (x86)\\Python39-32\\lib\\collections\\abc.py'
```

## Notes
- Intended for use in python-3.7 and up and LabVIEW 2021 and up.
- If using 64-bit LabVIEW, then use 64-bit python.
- If using 32-bit LabVIEW, then use 32-bit python.

## To Distribute In Development

    # Make .whl file in current folder
    pip wheel .

    # Install the generated .whl file (using the version you built)
    pip install labview_utils-0.1.0-py3-none-any.whl

