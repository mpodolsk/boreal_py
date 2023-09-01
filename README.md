# BOREAL python
This is python port of [boreal rust lib](https://github.com/vthib/boreal) which is a pure implementation of [YARA](https://yara.readthedocs.io/en/stable/) in rust.
It is a substitute for using [yara-python](https://github.com/VirusTotal/yara-python). As boreal is write in pure Rust we use [maturin /pyo3](https://www.maturin.rs/) to make a python wheel that does not need any special libs ot dynamic linking.


# using in python


```python

example_conent_rule = """
rule xxx_rule1
        {
            strings:
                $s1 = "hello"
            condition:
                filename endswith "test_file.txt" and $s1
        }
"""

def test_scanner():
    yara = boreal_py.Yara()
    yara.add_rules_str(example_conent_rule)
    yara.define_symbol("filename", "")
    scanner = yara.compile()
    results = scanner.scan_file("text.txt", {"filename": "text.txt"})


```


## local development and test
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -U pip maturin
(.venv) $ pip freeze
maturin==0.14.0
tomli==2.0.1
$ ./test.sh
```

