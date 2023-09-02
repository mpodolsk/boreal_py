import boreal_py
import os


test_dir = os.path.dirname(os.path.realpath(__file__))

example_conent_rule = """
rule xxx_rule1
        {
            strings:
                $s1 = "hello"
            condition:
                filename endswith "blob_of_data.txt" and $s1
        }
rule xxx_rule2
        {
            strings:
                $s1 = "hello"
            condition:
                filename endswith "blob_of_data.txt" and $s1
        }
rule yyy_rule1
        {
            strings:
                $s1 = "hello"
            condition:
                filename endswith "blob_of_data.txt" and $s1
        }
"""

def test_scanner():
    yara = boreal_py.YaraRules()
    yara.add_rules_str(example_conent_rule)
    yara.define_symbol("filename", "")
    scanner = yara.compile()
    test_file = os.path.abspath(test_dir + "/blob_of_data.txt")
    print(test_file)
    results = scanner.scan_file(test_file, {"filename": "blob_of_data.txt"})
    print(results)
    assert(len(results) == 3)
