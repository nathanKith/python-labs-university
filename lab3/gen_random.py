import random


def gen_random(num_count, begin, end):
    for item in [random.randrange(begin, end + 1) for i in range(num_count)]:
        yield item
