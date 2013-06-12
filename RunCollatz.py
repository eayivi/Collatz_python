#!/usr/bin/env python

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# Enam Ayivi cs_username:eayivi uteid: aea787
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
