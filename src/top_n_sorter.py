from __future__ import division, print_function, absolute_import, unicode_literals

import heapq


class TopNSorter(object):
    def __init__(self, limit):
        self._heap = []
        self.limit = limit

    def insert(self, item):
        if len(self._heap) == self.limit:
            heapq.heappushpop(self._heap, item)
        else:
            heapq.heappush(self._heap, item)

    def result(self):
        h = self._heap[:]
        buf = []
        while h:
            buf.insert(0, heapq.heappop(h))
        return buf


def test():
    s = TopNSorter(5)
    assert s.result() == []
    s.insert(10)
    assert s.result() == [10]
    s.insert(20)
    assert s.result() == [20, 10]
    s.insert(10)
    assert s.result() == [20, 10, 10]
    s.insert(5)
    assert s.result() == [20, 10, 10, 5]
    s.insert(30)
    assert s.result() == [30, 20, 10, 10, 5]
    s.insert(15)
    assert s.result() == [30, 20, 15, 10, 10]
    s.insert(10)
    assert s.result() == [30, 20, 15, 10, 10]
    s.insert(25)
    assert s.result() == [30, 25, 20, 15, 10]
    s.insert(1)
    assert s.result() == [30, 25, 20, 15, 10]
    print('ok')


if __name__ == '__main__':
    test()
