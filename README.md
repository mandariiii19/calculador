# Calculator
```markdown
# Natural Language Text Calculator

A robust Python-based text processing engine that parses, interprets, and evaluates mathematical expressions written entirely in natural language text (e.g., `"twenty five plus six multiplied by minus two"` / `"двадцать пять плюс шесть умножить на минус два"`). 

This project showcases structural parsing, lexical analysis, an implementation of operator precedence algorithms, and programmatic conversion between textual numerals and mathematical integer types.

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
