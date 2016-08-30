# partitions-of-set
4 python scripts which all do the same. namely generating all possible partitions of a set. e.g.: if you have a set "a", "b", "c", "d" then all possible partitions are:

[1, 1, 1, 1]
[1, 1, 1, 2]
[1, 1, 2, 1]
[1, 1, 2, 2]
[1, 1, 2, 3]
[1, 2, 1, 1]
[1, 2, 1, 2]
[1, 2, 1, 3]
[1, 2, 2, 1]
[1, 2, 2, 2]
[1, 2, 2, 3]
[1, 2, 3, 1]
[1, 2, 3, 2]
[1, 2, 3, 3]
[1, 2, 3, 4]

This approach is based on "a fast iterative algorithm for generating set partitions", The Computer Journal, Vol. 32, No. 3, 1989.

So such a partition called "codeword" from above like [1, 2, 1, 3] means:

 a  b  c  d

[1, 2, 1, 3]

a is in partition 1

b is in partition 2

c is in partition 1

d is in partition 3

There are 3 files:
partitions.setpart.py implements both proposed algorithms from the paper mentioned above. But they do not work!

partitions.tetrabase.recursive.py and partitions.tetrabase.iterative.py implement a new algorithm in the first the implementation is recursive in the latter one its iterative. Sure, the iterative one is faster. Further with this algorithm it is possible to define the maximum amount of partitions.
