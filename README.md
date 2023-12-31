# boreal_py

## About
This is python port of [boreal rust lib](https://github.com/vthib/boreal) which is a pure implementation of [YARA](https://yara.readthedocs.io/en/stable/) in rust.
It is a substitute for using [yara-python](https://github.com/VirusTotal/yara-python). As boreal is write in pure Rust we use [maturin /pyo3](https://www.maturin.rs/) to make a python wheel that does not need any special libs ot dynamic linking.




## using in python
Install from [pypi.org](https://pypi.org/project/boreal-py/)
```bash
$pip install boreal-py
```


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
    yara = boreal_py.YaraRules()
    yara.add_rules_str(example_conent_rule)
    yara.define_symbol("filename", "")
    scanner = yara.compile()
    results = scanner.scan_file("text.txt", {"filename": "text.txt"})


```


## local development and test
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install maturin
(.venv) pip install pytest
(.venv) $ pip freeze
maturin==0.14.0
tomli==2.0.1
$ ./test.sh
```

## build and publish
```bash
$docker run --rm -v $(pwd):/io ghcr.io/pyo3/maturin build --release --interpreter 3.11
$twine upload target/wheels/<build>

```