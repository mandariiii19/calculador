# Text Calculator

A natural-language arithmetic calculator that parses and evaluates mathematical expressions written entirely in Russian words — no digits, no symbols.

## Key Features

* **Natural Language Parsing**: Seamlessly translates word-based numbers into standard machine-readable numeric formats.
* **Complex Operator Precedence**: Evaluates multi-step arithmetic expressions with proper mathematical ordering (multiplication takes precedence over addition and subtraction).
* **Parentheses & Explicit Grouping**: Supports nested execution contexts via clear structural verbal indicators (`"скобка открывается"` / `"скобка закрывается"`).
* **Negative Numbers Engine**: Full support for negative values, both as inputs within the expression, intermediate processing steps, and final computed outcomes.
* **Robust Text Generator**: Features an inverse mapping algorithm that translates raw evaluation outcomes back into grammatically structured text.

---

## Supported Language Operations

The engine processes mathematical syntax through specific keyword mappings:

| Operational Element | Verbal Expression Mapping (Russian Syntax) | Equivalent Action |
| :--- | :--- | :--- |
| **Addition** | `плюс` | $+$ |
| **Subtraction** | `минус` | $-$ |
| **Multiplication** | `умножить` / `умножить на` | $\times$ |
| **Left Grouping** | `скобка открывается` | $($ |
| **Right Grouping** | `скобка закрывается` | $)$ |

---

## How It Works

```
Input string
     ↓
  Tokenizer        "двадцать шесть плюс пять"
     ↓              → [26, '+', 5]
  Parser           builds AST with correct precedence
     ↓
  Evaluator        computes result
     ↓
  Formatter        42 → "сорок два"
```

The parser handles operator precedence correctly — multiplication binds tighter than addition and subtraction — using a standard recursive descent approach. Parentheses are resolved before any other operations.

---

## Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/text-calculator.git
cd text-calculator
python calculator.py
```

Or import directly:

```python
from calculator import calc

result = calc("десять минус пять умножить на два минус шесть")
print(result)  # минус шесть
```

---

## Examples

```python
# Basic
calc("шесть плюс пять")                          # → "одиннадцать"
calc("двадцать шесть минус четыре")              # → "двадцать два"

# Operator precedence
calc("десять минус пять умножить на два минус шесть")   # → "минус шесть"
calc("два плюс три умножить на четыре")          # → "четырнадцать"

# Parentheses
calc("скобка открывается пять минус шесть скобка закрывается умножить на семь минус два")
# → "минус девять"

# Negative numbers
calc("пять минус минус шесть")                   # → "одиннадцать"
calc("ноль минус минус три")                     # → "три"
```

---

## Project Structure

```
text-calculator/
├── calculator.py       # Main calc() function — entry point
├── tokenizer.py        # Word → token conversion
├── parser.py           # Recursive descent parser, AST builder
├── evaluator.py        # AST evaluation with precedence
├── formatter.py        # Integer → Russian word string
└── tests/
    └── test_calc.py    # Unit tests for all features
```

---

## Author

**Manaeva Daria** 

