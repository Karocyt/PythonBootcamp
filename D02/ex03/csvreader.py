#! /usr/bin/env python3

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.bad = False
        self.file = open(filename, 'r')
        if not self.file:
            self.bad = True
        if not self.bad:
            self.data = [line.split(sep)
                         for line in self.file.read().splitlines()]
            self.sep = sep
            self.curr = skip_top
            self.stop = min(len(self.data), len(self.data) - skip_bottom)
            if header:
                self.header = self.getline()
            else:
                self.header = None
            self.builddata()

    def getdata(self):
        return self.data

    def builddata(self):
        ret = []
        size = len(self.header) if self.header else None
        line = self.getline()
        while line:
            values = line
            if not size:
                size = len(values)
            elif len(values) is not size:
                self.bad = True
                return
            indexes = self.header if self.header else range(0, len(values))
            elem = None
            if self.header:
                elem = {}
            else:
                elem = []
            for field, val in zip(indexes, values):
                if self.header:
                    elem[field] = val
                else:
                    elem += [val]
            ret += [elem]
            line = self.getline()
        self.data = ret

    def getline_iterator(self):
        if self.curr >= self.stop:
            yield self.getline()

    def getline(self):
        if self.curr >= self.stop:
            return None
        ret = self.data[self.curr]
        self.curr += 1
        return ret

    def getheader(self):
        return self.header

    def __enter__(self):
        if self.bad:
            return None
        return self

    def __exit__(self, *args):
        self.file.close()


if __name__ == "__main__":
    print("\ntest1")
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print("header:\n", header, "\ndata:\n", data)

    print("\ntest2")
    with CsvReader('good.csv', header=True) as file:
        data = file.getdata()
        header = file.getheader()
        print("header:\n", header, "\ndata:\n", data)

    print("\ntest3")
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
