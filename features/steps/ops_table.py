# -- FILE: features/steps/ops_table.feature
from lib.assertions import assertItemsEqual

@then(u"I will see the following table")
def then_compare_tables(context):
    expected = context.table
    assert expected, "Ensure table is provided."
    observed = context.result
    assertItemsEqual(list(observed.columns), expected.headings, "Headings do not match.")
    assert len(expected.rows) == len(observed), "Number of rows does not match."
    for i in range(len(expected.rows)):
        assertItemsEqual(list(observed.loc[i]), list(expected.rows[i]), "Rows do not match in content.")