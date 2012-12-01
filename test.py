import lxml.html
import parse

def _(fixture_name):
    'Base test'
    html = lxml.html.parse('fixtures/' + fixture_name + '.html')
    data = parse._parse_table(html)
    observed = parse._csv(data)
    expected = open('fixtures/' + fixture_name + '.csv').read()

def test_1():
    _('WestBengal_2005.aspx')
