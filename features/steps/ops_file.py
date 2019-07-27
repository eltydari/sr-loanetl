# -- FILE: features/steps/ops_file.feature
import os.path
import json

@given(u"a file named \"{fileName}\" with")
def given_named_file_containing(context, fileName):
    dir = context.dir.name
    with open(os.path.join(context.dir.name, fileName), 'w') as f:
        f.write(context.text)


@given(u"a map with the following representation")
def given_map_containing(context):
    context.map = json.loads(context.text)