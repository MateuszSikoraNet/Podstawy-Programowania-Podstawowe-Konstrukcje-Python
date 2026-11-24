from collections import deque


class DataStructureTools:
    def slices(self, values):
        # Return the tuple (values[1:3], values[-2:], values[::2], values[::-1]).
        # A slice is [start:stop:step]; stop is excluded, negative indexes count from the end, and the original is not changed.
        pass

    def edit_list(self, values):
        # Change values in place: append 4, insert 0 at the front, remove the first 2, extend with [5, 6].
        # Then pop the last element and return it. remove() raises ValueError if 2 is missing.
        pass

    def run_stack(self, operations):
        # A stack is last in, first out (LIFO). Use a list: append() to push, pop() to pop.
        # operations is a list of ("push", value) or ("pop",). Return the popped values in order.
        # Popping an empty stack raises IndexError.
        pass

    def run_queue(self, operations):
        # A queue is first in, first out (FIFO). Use collections.deque: append() to enqueue, popleft() to dequeue.
        # operations is a list of ("push", value) or ("pop",). Return the dequeued values in order.
        # Popping an empty queue raises IndexError.
        pass

    def pop_key(self, mapping, key):
        # Remove key from mapping and return its value (mapping.pop(key)). A missing key raises KeyError.
        pass

    def dict_views(self, mapping):
        # Return the tuple (list of keys, list of values, list of (key, value) pairs), in insertion order.
        pass

    def edit_set(self, items):
        # Change the set in place: add 4, discard 99 (no error if missing), then remove 1 (KeyError if missing).
        # Return nothing.
        pass

    def head_and_tail(self, values):
        # Return (first, rest) using star unpacking: first, *rest = values. rest is always a list.
        # An empty sequence raises ValueError (nothing to unpack into first).
        pass

    def frequencies(self, values):
        # Return a dict mapping each value to how many times it appears, in order of first appearance.
        pass

    def group_by_length(self, words):
        # Return a dict of lists: word length -> words of that length, in their original order (a nested structure).
        pass

    def names_sorted_by_age(self, people):
        # people is a list of dicts like {"name": "Ada", "age": 36}. Return the names from youngest to oldest.
        # People of the same age keep their original order (sorted() is stable). Do not change people.
        pass

    def sort_and_reverse(self, values):
        # Call values.sort(), then values.reverse(), and return the tuple of what the two calls returned.
        # Both change the list in place and return None - so "values = values.sort()" would lose the list.
        pass

    def edit_slices(self, values):
        # Change values in place: replace values[1:3] with ["a", "b", "c"] (a slice can get a different number
        # of elements), then del values[0], then del values[-2:]. Return nothing.
        pass

    def remove_negatives_in_place(self, values):
        # Remove the negative numbers from values in place - the caller's list must change. Return nothing.
        # Do not call remove() while looping over the same list: the next element gets skipped.
        # Build the result and assign it to the whole slice instead: values[:] = [...].
        pass

    def pop_first_and_clear(self, values):
        # Remove and return the first element with values.pop(0), then empty the list with values.clear().
        # clear() empties the same object, so every other name for this list sees it empty (values = [] would not).
        # pop() on an empty list raises IndexError.
        pass

    def edit_dict(self, mapping):
        # Change mapping in place, in this order: mapping["a"] = 1 (adds or overwrites - an existing key keeps its place),
        # mapping.update({"b": 2, "c": 3}), mapping.setdefault("a", 100) (a exists, so nothing changes),
        # mapping.setdefault("d", 4) (d is missing, so it is added), del mapping["c"].
        # Then return mapping.popitem() - it removes and returns the last inserted (key, value) pair.
        pass

    def empty_groups(self, keys):
        # Return a dict that maps every key to its own new empty list.
        # dict.fromkeys(keys, []) would give every key the SAME list object - appending to one would change all.
        pass

    def remove_zero_values(self, mapping):
        # Delete every key whose value is 0 from mapping, in place. Return nothing.
        # Deleting keys while looping over the dict itself raises RuntimeError - loop over list(mapping) instead.
        pass

    def keys_by_value(self, mapping):
        # Return the keys sorted by their values, largest first. Keys with equal values keep their dict order.
        # Use sorted(mapping.items(), key=...) or sorted(mapping, key=mapping.get).
        pass

    def get_path(self, data, keys, default=None):
        # data is a nested dict, e.g. {"a": {"b": 1}}. Follow keys one level at a time: get_path(data, ["a", "b"]) -> 1.
        # Return default if a key is missing or a value on the way is not a dict.
        pass

    def copy_and_clear(self, mapping):
        # Make backup = mapping.copy(), then empty mapping with mapping.clear(). Return backup.
        # The copy is a separate dict, so it keeps its items - but it is shallow: nested lists/dicts are shared, not copied.
        pass

    def tuple_methods(self, values, item):
        # Return (values.count(item), values.index(item)) - a tuple has only these two methods.
        # index() raises ValueError if item is missing.
        pass

    def sort_pair(self, a, b):
        # Return (a, b) with the smaller value first. Swap with tuple unpacking: a, b = b, a.
        pass

    def describe_point(self, point):
        # point looks like ((x, y), label). Unpack it in one step: (x, y), label = point.
        # Return f"{label} at {x},{y}". A wrong number of values raises ValueError.
        pass

    def count_by_cell(self, points):
        # points is a list of (x, y) tuples. Return a dict counting each point - tuples can be dict keys
        # because they are immutable and hashable (lists cannot).
        pass

    def summarize(self, collection):
        # Return (len, min, max, sorted list) of any collection - list, tuple, set, str or dict.
        # The same built-in functions work on every collection; for a dict they use its keys.
        pass

    def any_all_negative(self, values):
        # Return (any value is negative, all values are negative) using any() and all().
        # For an empty collection any() is False and all() is True (nothing breaks the rule).
        pass

    def longest_word(self, words):
        # Return the longest word with max(words, key=len). On a tie the first one wins.
        # An empty list raises ValueError (as max() does).
        pass
