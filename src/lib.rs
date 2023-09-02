use std::collections::HashMap;

use boreal::Scanner;
use pyo3::prelude::*;

#[pyclass]
pub struct YaraScanner {
    inner: Scanner,
}

#[pymethods]
impl YaraScanner {
    pub fn scan_file(
        &mut self,
        path: String,
        externals: HashMap<String, String>,
    ) -> PyResult<Vec<String>> {
        for k in externals.keys() {
            self.inner
                .define_symbol(k, String::from(externals.get(k).unwrap()))
                .unwrap();
        }
        let results = self.inner.scan_file(path).unwrap();

        return Ok(results
            .matched_rules
            .iter()
            .map(|r| String::from(r.name))
            .collect());
    }
}

#[pyclass]
struct YaraRules {
    raw_rules: String,
    externals: HashMap<String, String>,
}
#[pymethods]
impl YaraRules {
    #[new]
    pub fn new() -> PyResult<Self> {
        return Ok(Self {
            raw_rules: String::new(),
            externals: HashMap::new(),
        });
    }

    fn add_rules_str(&mut self, raw_rules: String) -> PyResult<()> {
        self.raw_rules = raw_rules;
        return Ok(());
    }

    fn define_symbol(&mut self, var_name: String, var_value: String) -> PyResult<()> {
        self.externals.insert(var_name, var_value);
        return Ok(());
    }
    fn compile(&mut self) -> YaraScanner {
        let mut comp = boreal::Compiler::new();
        for k in self.externals.keys() {
            comp.define_symbol(k, String::from(self.externals.get(k).unwrap()));
        }
        comp.add_rules_str(self.raw_rules.clone()).unwrap();
        return YaraScanner {
            inner: comp.into_scanner(),
        };
    }
}

#[pymodule]
fn boreal_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<YaraRules>()?;
    m.add_class::<YaraScanner>()?;
    Ok(())
}
