# Example: Debugging Session

## Context
Fix runtime error in Node.js.

## Error
TypeError: Cannot read property 'map' of undefined

---

## Prompt Used
(From coding/debug-code.md)

Analyze the code and error message. Identify root cause and fix.

---

## AI Diagnosis

- Data not validated before mapping
- Possible undefined API response

---

## Fix Suggested

```js
if (!Array.isArray(data)) {
  return [];
}
return data.map(...)
