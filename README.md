# Calculator UI Overview

This document summarizes the widgets and layout of the calculator UI.

---

## Main Window
- **Class:** `QMainWindow`
- **Name:** `MainWindow`
- **Size:** 568×288
- **Title:** MainWindow
- **Central Widget:** `centralwidget` (`QWidget`)

---

## Display
- **Widget:** `QLabel`
- **Name:** `display`
- **Font Size:** 20pt
- **Text:** "0"
- **Alignment:** Right, Vertical Center
- **Purpose:** Shows input and calculation results

---

## Layout
- **Main Layout:** `QVBoxLayout` → `verticalLayout`
- **Grid Layout for Buttons:** `QGridLayout` → `gridLayout`

---

## Number Buttons
- `n0` → 0
- `n1` → 1
- `n2` → 2
- `n3` → 3
- `n4` → 4
- `n5` → 5
- `n6` → 6
- `n7` → 7
- `n8` → 8
- `n9` → 9
- `dot` → "."

---

## Operator Buttons
- `o1` → "+"
- `o2` → "-"
- `o3` → "*"
- `o4` → "/"
- `o5` → "^"
- `o6` → "^2"
- `o7` → "^3"
- `upten` → "*10^"

---

## Memory Buttons
- `m0` → M+
- `m1` → M-
- `m2` → MRC
- `m3` → MC

---

## Special Buttons
- `pushButton` → π
- `pushButton_2` → Floor
- `pushButton_3` → Mod
- `ans` → Ans
- `AC` → AC
- `DEL` → DEL
- `calc` → exe

---

## Notes
- Buttons can be connected to functions using `.clicked.connect()`.
- `display` shows all current inputs and results.
- Memory and special buttons require custom handling logic.
