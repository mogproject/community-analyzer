#!/usr/bin/env python
from __future__ import division, print_function, absolute_import, unicode_literals

import sys
import fileinput
from top_n_sorter import TopNSorter


def join(data, absorbs, absorbed):
    if absorbed == -1:
        return data

    if absorbed not in data:
        data[absorbed] = {absorbed}
    if absorbs in data:
        data[absorbed] |= data[absorbs]
        del data[absorbs]
    else:
        data[absorbed].add(absorbs)
    return data


def num_clusters(data, limit=10):
    sorter = TopNSorter(limit)
    for index in data:
        sorter.insert(len(data[index]))
    return sorter.result()


def main(argv):
    max_q = 0.0
    max_q_step = 0
    data = {}
    for line in fileinput.input(argv[1:]):
        (absorbs, absorbed, q, step) = line.rstrip().split('\t')
        absorbs = int(absorbs)
        absorbed = int(absorbed)
        q = float(q)
        step = int(step)
        data = join(data, absorbs, absorbed)

        # print the number of clusters (top 10)
        if step % 10000 == 0:
            print(step, q, num_clusters(data))

        # update max Q
        if max_q < q:
            max_q = q
            max_q_step = step

    print('Max Q: %f (step=%d)' % (max_q, max_q_step))


if __name__ == '__main__':
    main(sys.argv)
