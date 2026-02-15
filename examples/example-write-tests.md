# Example: Generate Unit Tests

## Context
Add test coverage to a simple utility function.

## Input Code

```js
function divide(a, b) {
  if (b === 0) throw new Error("Division by zero");
  return a / b;
}
