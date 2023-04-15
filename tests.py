import pytest
from bloom_filter import BloomFilter


def test_bloom_filter():
    items = ["abc", "lzw", "rsa", "test", "1"]
    bloom_filter = BloomFilter(5, 0.05)
    
    for item in items:
        bloom_filter.add(item)

    for item in items:
        assert item in bloom_filter


def test_bloom_filter_from_iterable():
    items = ["abc", "lzw", "rsa", "test", "1"]
    bloom_filter = BloomFilter.from_iterable(items)
    
    for item in items:
        assert item in bloom_filter


def test_bloom_filter_exceeded():
    bloom_filter = BloomFilter(3)

    for item in range(3):
        bloom_filter.add(item)
    
    with pytest.raises(ValueError):
        bloom_filter.add(42)