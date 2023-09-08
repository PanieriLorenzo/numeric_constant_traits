lel = [
    ("u8", int),
    ("u16", int),
    ("u32", int),
    ("u64", int),
    ("u128", int),
    ("usize", int),
    ("i8", int),
    ("i16", int),
    ("i32", int),
    ("i64", int),
    ("i128", int),
    ("isize", int),
    ("f32", float),
    ("f64", float),
]


for n in range(2, 101):
    print("[", end="")
    for p in lel:
        print(f"{p[1](n)}, ", end="")
    print("],")
