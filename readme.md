We start at [this page](http://nirmalgrampuraskar.nic.in/Report/RptGPAwardedSummaryTill2010.aspx).
That has a bunch of state names. Clicking one state gets to another table.
That other table has a "Total" link at the end. We want that page.
We want these columns in the final dataset

* Year
* State Name
* District Name
* Block Name
* Panchayat Name 

Start selenium like so

    java -jar selenium-server-standalone-2.26.0.jar -port 4443

But actually, we're going to download the pages manually and then write the
parser.
