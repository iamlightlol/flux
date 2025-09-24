# flux/stdlib.py
# Flux standard library (100+ functions)
# Keep this purely Python so the interpreter can inject EXPORTS.

import math
import random
import time
import os
import uuid
import json
import threading
import urllib.request
import urllib.parse
from functools import reduce
from statistics import mean, median, variance, stdev

# ----------------------
# Math (22)
# ----------------------
def sqrt(x): return math.sqrt(x)
def pow_(a, b): return math.pow(a, b)
def abs_(x): return abs(x)
def floor(x): return math.floor(x)
def ceil(x): return math.ceil(x)
def round_(x, n=0): return round(x, n)
def log(x, base=math.e): return math.log(x, base) if base else math.log(x)
def exp(x): return math.exp(x)
def sin(x): return math.sin(x)
def cos(x): return math.cos(x)
def tan(x): return math.tan(x)
def factorial(n): return math.factorial(n)
def gcd(a, b): return math.gcd(a, b)
def lcm(a, b): 
    if hasattr(math, "lcm"):
        return math.lcm(a, b)
    return abs(a*b) // math.gcd(a, b)
def deg(x): return math.degrees(x)
def rad(x): return math.radians(x)
def isclose(a, b, rel_tol=1e-9, abs_tol=0.0): return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
def max_(iterable, *args): return max(iterable, *args)
def min_(iterable, *args): return min(iterable, *args)
def sum_(iterable): return sum(iterable)
def mean_(iterable): return mean(iterable)
def median_(iterable): return median(iterable)
def variance_(iterable): return variance(iterable)

# ----------------------
# Strings (16)
# ----------------------
def to_str(x=""): return str(x)
def upper(s): return str(s).upper()
def lower(s): return str(s).lower()
def strip(s): return str(s).strip()
def lstrip(s): return str(s).lstrip()
def rstrip(s): return str(s).rstrip()
def replace(s, old, new, count=-1): 
    return str(s).replace(old, new, len(str(s)) if count == -1 else count)
def split(s, sep=None, maxsplit=-1): return str(s).split(sep, maxsplit)
def join(sep, seq): return str(sep).join(map(str, seq))
def startswith(s, prefix): return str(s).startswith(prefix)
def endswith(s, suffix): return str(s).endswith(suffix)
def find(s, sub): return str(s).find(sub)
def format_(s, /, *args, **kwargs): return str(s).format(*args, **kwargs)
def capitalize(s): return str(s).capitalize()
def title(s): return str(s).title()
def substring(s, start, end=None): return str(s)[start: end]

# ----------------------
# Collections / List helpers (26)
# ----------------------
def len_(x): return len(x)
def list_(x=()): return list(x)
def dict_(pairs=None): 
    if pairs is None: return {}
    return dict(pairs)
def append(lst, x):
    lst.append(x); return lst
def pop(lst, idx=-1): return lst.pop(idx)
def sort(lst, key=None, reverse=False): lst.sort(key=key, reverse=reverse); return lst
def sorted_(iterable, key=None, reverse=False): return sorted(iterable, key=key, reverse=reverse)
def reverse(lst): lst.reverse(); return lst
def range_(a, b=None, step=1):
    if b is None: return list(range(a))
    return list(range(a, b, step))
def map_(fn, iterable): return list(map(fn, iterable))
def filter_(fn, iterable): return list(filter(fn, iterable))
def reduce_(fn, iterable, initial=None):
    if initial is None: return reduce(fn, iterable)
    return reduce(fn, iterable, initial)
def zip_(*iterables): return list(zip(*iterables))
def enumerate_(iterable, start=0): return list(enumerate(iterable, start))
def unique(seq):
    seen = set(); out = []
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out
def flatten(list_of_lists): 
    out = []
    for sub in list_of_lists:
        out.extend(list(sub))
    return out
def chunk(lst, n): 
    if n <= 0: return [lst[:]]
    return [lst[i:i+n] for i in range(0, len(lst), n)]
def first(xs): return xs[0] if xs else None
def last(xs): return xs[-1] if xs else None
def contains(seq, x): return x in seq
def index_of(seq, x): return seq.index(x) if x in seq else -1
def count_of(seq, x): return seq.count(x)
def clear(seq): 
    seq.clear(); return seq
def copy_(seq): 
    import copy
    return copy.deepcopy(seq)
def push(lst, x): lst.append(x); return lst
def pop_front(lst): return lst.pop(0) if lst else None

# ----------------------
# IO & Filesystem (12)
# ----------------------
def print_(*args, **kwargs): 
    # wrapper to behave like print but name-safe
    print(*args, **kwargs)
def input_(prompt=""): return input(prompt)
def read_file(path, mode="r", encoding="utf-8"):
    with open(path, mode, encoding=encoding) as f:
        return f.read()
def write_file(path, data, mode="w", encoding="utf-8"):
    with open(path, mode, encoding=encoding) as f:
        f.write(str(data)); return True
def append_file(path, data, encoding="utf-8"):
    with open(path, "a", encoding=encoding) as f:
        f.write(str(data)); return True
def exists(path): return os.path.exists(path)
def cwd(): return os.getcwd()
def listdir(path="."): return os.listdir(path)
def mkdir(path, exist_ok=False): return os.makedirs(path, exist_ok=exist_ok)
def remove(path): return os.remove(path)
def rename(src, dst): return os.rename(src, dst)
def stat(path): return os.stat(path)

# ----------------------
# Time & Random (7)
# ----------------------
def time_now(): return time.time()
def sleep(seconds): return time.sleep(seconds)
def random_(): return random.random()
def randint(a, b): return random.randint(a, b)
def choice(seq): return random.choice(seq)
def shuffle(seq): random.shuffle(seq); return seq
def uuid4(): return str(uuid.uuid4())

# ----------------------
# JSON & HTTP (6)
# ----------------------
def json_dumps(obj, **kwargs): return json.dumps(obj, **kwargs)
def json_loads(s): return json.loads(s)
def http_get(url, timeout=10, headers=None):
    req = urllib.request.Request(url, headers=(headers or {}), method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode()
def http_post(url, data=None, timeout=10, headers=None):
    body = None
    if data is not None:
        if isinstance(data, (dict, list)):
            body = json.dumps(data).encode()
            headers = dict(headers or {})
            headers.setdefault("Content-Type", "application/json")
        else:
            body = str(data).encode()
    req = urllib.request.Request(url, data=body, headers=(headers or {}), method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode()
def url_encode(params): return urllib.parse.urlencode(params)
def url_decode(qs): return dict(urllib.parse.parse_qsl(qs))

# ----------------------
# Concurrency (6)
# ----------------------
def spawn_thread(fn, *args, daemon=True, **kwargs):
    t = threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=daemon)
    t.start(); return t
def run_in_thread(fn, *args, **kwargs):
    return spawn_thread(fn, *args, **kwargs)
def join_thread(thread, timeout=None): thread.join(timeout); return thread.is_alive()
def lock(): return threading.Lock()
def Event(): return threading.Event()
def sleep_ms(ms): time.sleep(ms/1000.0)

# ----------------------
# Misc utilities (7)
# ----------------------
def echo(x): print(x); return x
def noop(*a, **k): return None
def identity(x): return x
def clamp(x, a, b): return max(a, min(b, x))
def retry(fn, tries=3, delay=0.1, exceptions=(Exception,)):
    last = None
    for i in range(tries):
        try:
            return fn()
        except exceptions as e:
            last = e
            time.sleep(delay)
    raise last
def chunked_iterable(it, chunk_size):
    it = iter(it)
    while True:
        chunk = []
        for _ in range(chunk_size):
            try:
                chunk.append(next(it))
            except StopIteration:
                break
        if not chunk: break
        yield chunk

# ----------------------
# EXPORTS mapping
# ----------------------
EXPORTS = {
    # math
    "sqrt": sqrt, "pow": pow_, "abs": abs_, "floor": floor, "ceil": ceil,
    "round": round_, "log": log, "exp": exp, "sin": sin, "cos": cos, "tan": tan,
    "factorial": factorial, "gcd": gcd, "lcm": lcm, "deg": deg, "rad": rad,
    "isclose": isclose, "max": max_, "min": min_, "sum": sum_, "mean": mean_,
    "median": median_, "variance": variance_,

    # strings
    "str": to_str, "upper": upper, "lower": lower, "strip": strip, "lstrip": lstrip,
    "rstrip": rstrip, "replace": replace, "split": split, "join": join, "startswith": startswith,
    "endswith": endswith, "find": find, "format": format_, "capitalize": capitalize,
    "title": title, "substring": substring,

    # collections
    "len": len_, "list": list_, "dict": dict_, "append": append, "pop": pop,
    "sort": sort, "sorted": sorted_, "reverse": reverse, "range": range_, "map": map_,
    "filter": filter_, "reduce": reduce_, "zip": zip_, "enumerate": enumerate_,
    "unique": unique, "flatten": flatten, "chunk": chunk, "first": first, "last": last,
    "contains": contains, "index": index_of, "count": count_of, "clear": clear,
    "copy": copy_, "push": push, "pop_front": pop_front,

    # io
    "print": print_, "input": input_, "read_file": read_file, "write_file": write_file,
    "append_file": append_file, "exists": exists, "cwd": cwd, "listdir": listdir,
    "mkdir": mkdir, "remove": remove, "rename": rename, "stat": stat,

    # time/random
    "time_now": time_now, "sleep": sleep, "sleep_ms": sleep_ms, "random": random_,
    "randint": randint, "choice": choice, "shuffle": shuffle, "uuid4": uuid4,

    # json/http
    "json_dumps": json_dumps, "json_loads": json_loads, "http_get": http_get,
    "http_post": http_post, "url_encode": url_encode, "url_decode": url_decode,

    # concurrency
    "spawn_thread": spawn_thread, "run_in_thread": run_in_thread, "join_thread": join_thread,
    "lock": lock, "Event": Event,

    # misc
    "echo": echo, "noop": noop, "identity": identity, "clamp": clamp,
    "retry": retry, "chunked_iterable": chunked_iterable,
}
