source .venv/bin/activate
rm -rf target/
maturin develop
python3 -m pytest -s tests_python/




