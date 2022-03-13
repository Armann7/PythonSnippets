

def mycmp(a: str, b: str) -> int:
    al = list(map(int, a.split(sep='.')))
    bl = list(map(int, b.split(sep='.')))
    while len(al) > 0 or len(bl) > 0:
        av = al.pop(0) if len(al) > 0 else 0
        bv = bl.pop(0) if len(bl) > 0 else 0
        if av > bv:
            return 1
        if av < bv:
            return -1
    return 0


assert mycmp('1', '2') == -1
assert mycmp('2', '1') == 1
assert mycmp('1', '1') == 0
assert mycmp('1.0', '1') == 0
assert mycmp('1', '1.000') == 0
assert mycmp('12.01', '12.1') == 0
assert mycmp('13.0.1', '13.00.02') == -1
assert mycmp('1.1.1.1', '1.1.1.1') == 0
assert mycmp('1.1.1.2', '1.1.1.1') == 1
assert mycmp('1.1.3', '1.1.3.000') == 0
assert mycmp('3.1.1.0', '3.1.2.10') == -1
assert mycmp('1.1', '1.10') == -1
assert mycmp("0.1", "1.1") == -1
assert mycmp("1.0.1", "1") == 1
assert mycmp("7.5.2.4", "7.5.3") == -1
assert mycmp("1.01", "1.001") == 0
assert mycmp("1.0", "1.0.0") == 0
assert mycmp("2", "2.0.0") == 0
assert mycmp("1.01", "1.101") == -1
