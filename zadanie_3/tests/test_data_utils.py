
from my_awesome_lib.data_utils import load_csv, flatten_dict

def test_load_csv_returns_list_of_dicts():
    with tempfile.NamedTemporaryFile('w+', newline='', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age'])
        writer.writerow(['Ada', '30'])
        writer.writerow(['Bob', '25'])
        fname = f.name

    rows = load_csv(fname)
    os.remove(fname)
    assert rows == [{'name': 'Ada', 'age': '30'},
                    {'name': 'Bob', 'age': '25'}]

def test_flatten_dict_nested():
    src = {'a': {'b': 1, 'c': {'d': 2}}, 'e': 3}
    flat = flatten_dict(src)
    assert flat == {'a.b': 1, 'a.c.d': 2, 'e': 3}
