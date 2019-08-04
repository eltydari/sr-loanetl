# -- FILE: features/steps/io.py
import json
import nose.tools as testing
import os.path
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
    context.cfg = json.loads(context.text)

@then(u"I will see the following table")
def then_compare_tables(context):
    expected = context.table
    testing.assert_true(expected, "Please ensure table is provided")
    observed = context.result
    testing.assert_count_equal([str(x) for x in observed.columns], expected.headings)
    testing.assert_equals(len(expected.rows), len(observed))
    for i in range(len(expected.rows)):
        testing.assert_count_equal([str(x) for x in observed.loc[i].tolist()], 
                                     list(expected.rows[i]))