tracegraph
==========

A wrapper around `traceroute` that will draw charts from the ping data.

A graphical representation of the ping delays helps in much more quickly
identifying bottlenecks than parsing the output of traceroute in your head.

Currently only tested on Mac OS X, so needs BSD-compatible traceroute output.

Usage
=====

Either pipe the output of `traceroute` into this program, or invoke it as you
would normally invoke `traceroute` and the parameters will be passed on.

Requires Python 2.x.

Example
=======

For best results, symlink `tracegraph.py` into `/usr/local/bin`:

    $ ln -s ~/tracegraph/tracegraph.py /usr/local/bin/tracegraph
    $ tracegraph www.av.com
        1  192.168.0.1 (192.168.0.1)  5.988 ms  2.686 ms  1.562 ms
        2  * * *
        3  109.255.253.1 (109.255.253.1)  12.454 ms  10.893 ms  8.578 ms
        4  84.116.238.114 (84.116.238.114)  26.098 ms  12.426 ms  23.640 ms
        5  nl-ams05a-rd2-xe-4-3-1.aorta.net (84.116.134.82)  16.221 ms
            84.116.134.130 (84.116.134.130)  9.160 ms
            84.116.134.178 (84.116.134.178)  9.563 ms
        6  ge-1-3-0.pat2.irz.yahoo.com (193.242.111.77)  10.889 ms  10.422 ms  10.081 ms
        7  ae-2.msr1.ird.yahoo.com (66.196.67.235)  10.272 ms
            ae-2.msr2.ird.yahoo.com (66.196.67.237)  9.981 ms
            ae-2.msr1.ird.yahoo.com (66.196.67.235)  21.167 ms
        8  te-8-4.bas-b1.ird.yahoo.com (87.248.101.107)  11.125 ms
            te-7-4.bas-b2.ird.yahoo.com (87.248.101.105)  9.435 ms
            te-8-4.bas-b2.ird.yahoo.com (87.248.101.109)  15.230 ms
        9  w2.rc.vip.ird.yahoo.com (77.238.178.122)  10.643 ms  12.369 ms  12.239 ms

        tracegraph:
        1 192.168.0.1          |   o---------o
        2 ?                    | 
        3 109.255.253.1        |                   o--------o
        4 84.116.238.114       |                            o-------------------------------o
        5 ...e-4-3-1.aorta.net |                                     o
          84.116.134.130       |                     o
          84.116.134.178       |                     o
        6 ...at2.irz.yahoo.com |                       o-o
        7 ...sr1.ird.yahoo.com |                       o
          ...sr2.ird.yahoo.com |                      o
          ...sr1.ird.yahoo.com |                                                o
        8 ...-b1.ird.yahoo.com |                         o
          ...-b2.ird.yahoo.com |                     o
          ...-b2.ird.yahoo.com |                                   o
        9 ...vip.ird.yahoo.com |                        o---o
                                0ms                                                     26.1ms
