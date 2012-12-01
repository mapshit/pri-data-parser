#!/usr/bin/env python
import json
import lxml.html

def _parse_table(html):
    'Parse a table from an html element'
    table = html.xpath('//table[@class="Table"]')[0]
    year = html.xpath('id("ctl00_ContentPlaceHolder1_lbl_gpAwdYr")/text()')[0].split(' ')[-1]
    trs = table.xpath('tr[position()>1]')
    data = []
    for tr in trs:
        row = _parse_row(tr)
        row['year'] = year
        data.append(row)
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
    out = 'Year,State Name,District Name,Block Name,Panchayat Name\r'
    for row in data:
        out += '%(year)s,%(state)s,%(district)s,%(block)s,%(panchayat)s\r' % row
    return out

def main(fixture_file):
    html = lxml.html.parse(fixture_file)
    data = _parse_table(html)
    return json.dumps(data)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        raise TypeError('USAGE: %s [html file]' % sys.argv[0])
