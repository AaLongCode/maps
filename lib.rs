use pyo3::prelude::*;
use serde::{Serialize, Deserialize};

#[pyfunction]
fn sum_as_string(a: i32, b: i32) -> PyResult<String> {
    Ok((a + b).to_string())
}
#[pyclass]
pub struct Node{
    key: u32,
    latitude: f32,
    longitude: f32,
    left:  Option<Box<Node>>,
    right: Option<Box<Node>>
}
#[pymethods]
impl Node{
    #[new]
    pub fn new(key:u32, latitude:f32,longitude:f32) -> Self{
        Node {key,latitude:latitude,longitude:longitude,left:None,right:None}
    }
    pub fn get_long(&self) -> f32 {
        self.longitude
    }
}
#[pyclass]
pub struct Btree{
    root: Option<Box<Node>>
}
#[pymethods]
impl Btree{
    #[new]
    fn new() -> Self{
        Btree {root: None}
    }
    fn add()
}


#[pymodule]
fn btree(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_class::<Node>()?;
    Ok(())
}