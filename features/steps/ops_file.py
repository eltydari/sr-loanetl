# -- FILE: features/steps/ops_file.feature
import os.path

@given(u"a file named \"{fileName}\" with")
def step_impl(context, fileName):
    dir = context.dir.name
    with open(os.path.join(context.dir.name, fileName), 'w') as f:
        f.write(context.text)