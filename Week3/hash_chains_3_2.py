# python2


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        # chained hash table
        self.chain_hash_table = [[]] * self.bucket_count

    def _hash_func(self, s):
        result = 0
        # string hash function
        for c in reversed(s):
            result = (result * self._multiplier + ord(c)) % self._prime
        # hash into chained table
        return result % self.bucket_count

    def write_search_result(self, was_found):
        print 'yes' if was_found else 'no'

    def write_chain(self, chain):
        print ' '.join(chain)

    def read_query(self):
        return Query(raw_input().split())

    def process_query_naive(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query_hash_chain(self, query):
        # Algorithm to implement chained hashing
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.chain_hash_table[query.ind]) if self._hash_func(cur) == query.ind)
        else:
            string_hash = self._hash_func(query.s)
            try:  # find index of s
                ind = self.chain_hash_table[string_hash].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.chain_hash_table[string_hash].append(query.s)
            else:  # delete
                if ind != -1:
                    self.chain_hash_table[string_hash].pop(ind)

    def process_queries(self):
        n = int(raw_input())
        for i in range(n):
            self.process_query_hash_chain(self.read_query())


if __name__ == '__main__':
    bucket_count = int(raw_input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


# line 1 = m = cardinality
# line 2 = n = size of commands
#
# i/p:
# 5
# 12
# add world
# add HellO
# check 4
# find World
# find world
# del world
# check 4
# del HellO
# add luck
# add GooD
# check 2
# del good
#
# o/p:
# HellO world
# no
# yes
# HellO
# GooD luck
