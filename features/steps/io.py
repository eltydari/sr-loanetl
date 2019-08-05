# -- FILE: features/steps/io.py
import json
import nose.tools as testing
import os.path
import unittest.mock as mock
import tempfile as tmp

@given(u"we have a folder")
def given_directory(context):
    context.dir = tmp.TemporaryDirectory()

@given(u"a file named \"{fileName}\" with")
def given_named_file_containing(context, fileName):
    dirName = context.dir.name
    with open(os.path.join(dirName, fileName), 'w') as f:
        f.write(context.text)

@given(u"a file named \"{fileName}\", with the \"%s\" placeholder representing my folder path")
def given_map_containing_placeholders(context, fileName):
    dirName = context.dir.name
    with open(os.path.join(dirName, fileName), 'w') as f:
        f.write(context.text % dirName)

@given(u"a configuration map with the following representation")
def given_map_containing(context):
    context.cfg = json.loads(context.text)

@given(u"a configuration map, with the \"%s\" placeholder representing my folder path")
def given_map_containing_placeholders(context):
    dirName = context.dir.name
    context.cfg = json.loads(context.text % dirName)

@when(u"I run the following command, with the placeholder representing my folder path")
def run_command_placeholders(context):
    from loan_etl.app.pipeline import run
    import shlex
    cmd = context.text.format(folder_path=context.dir.name)
    cfgDir = shlex.split(cmd)[1]
    with mock.patch("loan_etl.app.pipeline.DBLoader", return_value=context.db),\
         mock.patch("loan_etl.app.pipeline.getSchema", return_value=context.schema):
        run(cfgDir)

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