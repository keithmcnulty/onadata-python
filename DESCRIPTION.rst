# Overview

Project name: onadata-python

This package is port of an R package associated with the [free online](http://ona-book.org/) book _Handbook of Graphs and Networks in People Analytics_ by Keith McNulty. 

# Background

At ona-book.org, McNulty makes the data referenced in _Handbook of Graphs and Networks in People Analytics_ available [via an R package](https://cran.r-project.org/package=onadata). McNulty explains:

_For R and Python users, each of the data sets used in this book can be downloaded individually by following the code in each chapter. Alternatively for R users who intend to work through all of the chapters, all data sets can be loaded into an R session in advance by installing and loading the peopleanalyticsdata R package._

This package will bring the functionality of McNulty's R package to Python users. 

# Usage

```Python
# import onadata package
import onadata as ona
import pandas as pd

# see a list of data sets
ona.list_sets()

# find out more about a specific data set ('koenigsberg' example)
# ona.help(koenigsberg)

# load data into a dataframe
df = ona.koenigsberg()
```

# Data dictionary

The data dictionary pertinent to all the data sets can be found [here](https://cran.r-project.org/web/packages/onadata/onadata.pdf).

# LICENSE

- MIT
