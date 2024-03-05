A reproducible example of ArcGIS API for Python issue
<https://github.com/Esri/arcgis-python-api/issues/1769>.

First create a virtual environment and install the dependencies from
`requirements.txt`. (`requirements.txt` was compiled from
`pyproject.toml`; if you prefer to use a tool to install the
dependencies directly from `pyproject.toml`, it should yield the same
results.) Then run the `run_example.py` script. The following steps work
on Windows:

```ShellSession
git clone https://github.com/skykasko/arcgis-python-api-date-example
cd arcgis-python-api-date-example
py -3.9 -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py run_example.py
```

`run_example.py` will prompt you to enter a username and password to
login to ArcGIS Online. (To skip this, edit lines 11 and 12 of
`run_example.py` and enter the username and password directly in the
code.) It then creates a hosted ArcGIS Online feature layer with a
single feature based on the contents of `layer_source.csv`, which
contains two different date values in two date fields. Finally, it
attempts to update the date fields with two new, distinct date values.
