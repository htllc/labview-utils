# LabVIEW-Utils Package

## Notes
- Intended for use in python-3.7 and up and LabVIEW 2021 and up.
- If using 64-bit LabVIEW, then use 64-bit python.
- If using 32-bit LabVIEW, then use 32-bit python.

## To Distribute In Development

    # Make .whl file in current folder
    pip wheel .

    # Install the generated .whl file (using the version you built)
    pip install labview_utils-0.1.0-py3-none-any.whl

## Install from GitHub

    py -3.9-32 -m pip install git+ssh://git@github.com/htllc/labview-utils.git