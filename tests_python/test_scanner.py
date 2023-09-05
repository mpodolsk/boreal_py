import boreal_py
import os
import string
import random

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
# def gen_ran_str(length: int):
#     source = string.ascii_lowercase
#     source += string.ascii_uppercase
#     source += string.punctuation
#     source += string.digits
#     return ''.join(random.choice(source) for i in range(length))

# def setup_file():
#     with open('testing_blob','a+') as f:
#         for i in range(10000):
#             f.write(gen_ran_str(1000))    
#     return

# setup_file()


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
