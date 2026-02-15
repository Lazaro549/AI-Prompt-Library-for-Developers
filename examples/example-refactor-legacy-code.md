# Example: Refactor Legacy Code

## Context
Improve messy JavaScript code.

## Prompt Used
(From coding/refactor-code.md)

Refactor the following code to improve readability and maintainability while keeping functionality identical.

---

## Input

```js
function sumIfValid(a, b) {
  if (!a) return 0;
  return b ? a + b : a;
}
