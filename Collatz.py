#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------



# ------------
# cycle_length
# ------------

cycle_length_store = [0] * 100000

def cycle_length (n) :

    assert ( n > 0);
    valueToStore = n

    if (n < 100000 and cycle_length_store[n] !=0) :
        return cycle_length_store[n]
    else :
        c =1

        while (n>1) :
            if ( n%2 ==0) :
                n = n/2
            else :
                n = 3*n +1
            c = c+1
        if (valueToStore < 100000) :
            cycle_length_store [valueToStore] = c
        return c





# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <your code>

    if (j<i) :
        temp = j
        j=i
        i=temp

    if (i < j/2) :
        return collatz_eval(j/2,j);
    else :
        v = cycle_length(j)

        while (i <j) :
            temp_cycle = cycle_length(i)
            if (temp_cycle > v) :
                v = temp_cycle
            i = i+1

    return v




    #end of my code
    assert v > 0
    return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
