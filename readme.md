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

    cd data
    find . -exec ../msewage.sh {} \;
