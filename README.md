# Python OOP Complete Example

This project demonstrates **core Object-Oriented Programming (OOP) concepts in Python** through practical examples using a `Car` class hierarchy. It covers:

- **Encapsulation** (private attributes, getters/setters)
- **Inheritance** (single and multiple)
- **Polymorphism** (method overriding)
- **Static methods**
- **Object relationships and multiple inheritance**

---

## Classes Overview

### 1. `Car` (Base Class)
- Private attributes: `__brand`, `__model`
- Methods:
  - `get_brand()`, `get_model()`, `set_model()`
  - `car_details()`
  - `general_description()` (static method)

### 2. `ElectricCar` (Subclass of Car)
- Adds `__battery_capacity`
- Overrides `car_details()` and `start_engine()`

### 3. `HybridCar` (Subclass of Car)
- Adds `__fuel_capacity` and `__battery_capacity`
- Overrides `car_details()` and `start_engine()`

### 4. `SportsCar` (Multiple Inheritance)
- Inherits from `ElectricCar`, `Battery`, and `Engine`
- Demonstrates multiple inheritance with `batter_info()` and `engine_info()`

### 5. `Battery` and `Engine`
- Utility classes providing additional methods for multiple inheritance demonstration
