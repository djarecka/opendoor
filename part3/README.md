## This is a solution to a part 3

- I've built a simple memoize function to cash results.

- I've used OrderedDict as a container for results. OrderedDict have a popitem method that allows to remove items and keep a constant number of cashed results. OrderedDict allows for O(1) lookups, but the delete/insert operation is O(n) at worst.  