import parse

def test_data_equal(fixture_name):
    observed = parse.main('fixtures/' + fixture_name + '.html')
    expected = open('fixtures/' + fixture_name + '.csv').read()


