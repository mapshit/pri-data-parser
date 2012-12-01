import lxml.html
import parse
import nose.tools as n

def _(fixture_name):
    'Base test'
    html = lxml.html.parse('fixtures/' + fixture_name + '.html')
    data = parse._parse_table(html)
    observed = parse._csv(data)
    expected = open('fixtures/' + fixture_name + '.csv').read()
    observed_list = filter(None, observed.split('\r'))
    expected_list = filter(None, expected.split('\r'))
    n.assert_list_equal(observed_list, expected_list)

def test_1():
    _('WestBengal_2005.aspx')
