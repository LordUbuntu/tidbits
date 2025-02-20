# Jacobus Burger (2025-02-09)
# A web crawler to explore and graph social connections on GitHub from
#   a given user page for a specified graph depth, run in parallel
#   for faster performance.
# The start of a larger project that will get it's own repo once I figure
#   out a better name for it and have more time.

# Features:
# - command line utility
# - specify depth and other features to explore relational graphs
# - visualize graphs
# - parallelism for fast performance
# - basic API interaction with GitHub to be easy to use and change
import argparse                 # CLI
import multiprocessing as mp    # multiprocessing for faster execution
import graphviz as gv           # visualize connections
import requests as req          # getting requests from site
import bs4                      # parsing site


# I'll need to convert the adjacency list into a `.gv` file
# 
# digraph network {
#   layout=sfdp
#   a -> {b, c, d}
#   b -> {a, d, e}
# }
