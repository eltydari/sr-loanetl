# -- FILE: features/steps/ops_file.py
import os.path
import json
import tempfile as tmp

@given(u"we have a folder")
def given_directory(context):
    context.dir = tmp.TemporaryDirectory()

@given(u"a file named \"{fileName}\" with")
def given_named_file_containing(context, fileName):
    dir = context.dir.name
    with open(os.path.join(context.dir.name, fileName), 'w') as f:
        f.write(context.text)

@given(u"a configuration map with the following representation")
def given_map_containing(context):
    context.map = json.loads(context.text)