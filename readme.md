We start at [this page](http://nirmalgrampuraskar.nic.in/Report/RptGPAwardedSummaryTill2010.aspx).
That has a bunch of state names. Clicking one state gets to another table.
That other table has a "Total" link at the end. We want that page.
We want these columns in the final dataset

* Year
* State Name
* District Name
* Block Name
* Panchayat Name 

We downloaded the pages manually, and we have a thingy to convert them to the
msewage format. Install the
[msewage importer](https://github.com/jcmuller/msewage-importer).

    gem install msewage-importer

Then run something like this.

    . activate
    cd data
    find . -exec msewage.sh {} \;

Or to generate a csv

    . activate
    cd data
    echo Year,State Name,District Name,Block Name,Panchayat Name > ../pri.csv
    find . -name *.html -exec csv.sh {} \; >> ../pri.csv

This string is useful for geocoding in CartoDB.

    {panchayat_name}, {block_name}, {district_name}, {state_name}, India

[Here](http://tlevine.cartodb.com/tables/pri/embed_map?title=true&description=true&search=false&shareable=false&sql=&zoom=3&center_lat=25.958044673317843&center_lon=75.76171875)'s the map.
