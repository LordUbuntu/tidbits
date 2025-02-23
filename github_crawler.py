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


# some properties are known about the graph G of GitHub user relations:
# 1. it is a digraph
# 2. it may be cyclical on some subgraphs
# 3. each vertex may be isolated or in some subgraph

# graphviz
# G = gz.DiGraph()
# recursively:
#   G.node(root)
#   G.node(neighbour1)
#   G.edge(root, neighbour1)
#   ...
#   G.node(neighbourN)
#   G.edge(root, neighbourN)
# at the end:
#   G.render(filename=output_name_arg, format=format_arg)

# algorithm:
# - start at current node URL (top of multiprocessing pool queue) (a queue is used to avoid a runaway process)
# - wait for 50ms or so
# - scrape its page for current node username, add this node to graphviz with that name
# - scrape its page for followers / following URLs
# - test connection to that URL and ignore if it fails, otherwise add to queue
# - also add each connected neighbour name to graphviz, and add an edge from current node towards those neighbours
# - explore breadth first search, keeping below a limit defined by the depth argument (or not if an argument of -1 is given)
