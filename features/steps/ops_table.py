# -- FILE: features/steps/ops_table.feature

@then(u"I will see the following table")
def then_compare_tables(context):
    assert context.table, "Ensure table is provided."
    