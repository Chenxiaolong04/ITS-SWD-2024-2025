# Comparison of Array Methods: `slice()` vs `splice()`

## Overview

These JavaScript array methods serve different purposes:

- **`slice()`** → Copies a portion of an array  
- **`splice()`** → Modifies the original array

## Key Differences

| Feature        | `slice()`                          | `splice()`                        |
|----------------|-----------------------------------|-----------------------------------|
| **Mutates Original** | No (creates new array)            | Yes (modifies original)           |
| **Returns**         | New array with selected elements  | Array of removed elements         |
| **Main Purpose**    | Extract elements                  | Add/remove/replace elements       |

## Parameters

### `slice(start, end)`
- `start`: Beginning index (inclusive)
- `end`: Ending index (exclusive)  
  *(Both parameters are optional)*

### `splice(start, deleteCount, ...items)`
- `start`: Index to begin changes
- `deleteCount`: Number of elements to remove  
- `...items`: Elements to insert  
  *(Only start is required)*

