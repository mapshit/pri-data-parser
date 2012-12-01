def _parse_table(html):
    'Parse a table from an html element'
    table = html.xpath('//table[@class="Table"]')
    year = html.xpath('id("ctl00_ContentPlaceHolder1_lbl_gpAwdYr")/text()')[0].split(' ')[-1]
    trs = table.xpath('tr[position()>1]')
    data = []
    for tr in trs:
        row = _parse_row(tr)
        row['year'] = year
    return data

def _parse_row(tr):
    state = tr.xpath('td[position()=2]/text()')[0].strip()
    district = tr.xpath('td[position()=3]/text()')[0].strip()
    block = tr.xpath('td[position()=4]/text()')[0].strip()
    panchayat = tr.xpath('td[position()=5]/text()')[0].strip()
    return {
        "state": state,
        "district": district,
        "block": block,
        "panchayat": panchayat,
    }

def _csv(data):
    out = ''
    for row in data:
        out += '%s(year)s, %(state)s, %(district)s, %(block)s, %(panchayat)s' % row
    return out

def main(fixture_file):
    html = lxml.html.parse(fixture_file)
    data = _parse_table(html)
    return json.dumps(data)
