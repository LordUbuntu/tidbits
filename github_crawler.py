# Jacobus Burger (2025-02-09)
# A web crawler to explore and graph social connections on GitHub from
#   a given user page for a specified graph depth, run in parallel
#   for faster performance.
# The start of a larger project that will get it's own repo once I figure
#   out a better name for it and have more time.

# Name Ideas:
# - "neighbourhood"
# - "git net"
# - "github graph"

# This version will be just a CLI tool to scan and visualize connections rapidly,
#   but in the future I'll do an interactive version with jupyter notebooks
#   and / or some framework like Dash


# Features:
# - command line utility with flags to specify exploration depth, output, and more
# - generate graphs as graphviz (.gz) files
# - record and store network links as .csv and other data formats
# - seperate jupyter notebook for interactive visualization demo using pyvis and ipysigma
# - multiprocessing queue for fast performance
import argparse                 # CLI
import multiprocessing as mp    # multiprocessing for faster execution
import graphviz as gv           # generate .gv and .svg files to render graph
import requests as req          # getting requests from site
import bs4                      # parsing site
