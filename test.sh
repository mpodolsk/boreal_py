source .venv/bin/activate
rm -rf target/
maturin develop
python -m pytest -s tests_python/




