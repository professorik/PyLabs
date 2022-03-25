# PyLabs
```mermaid
flowchart TD
  A[Test] --> B{Test};
  A[Test] --> C[Test];
  B -- Yes --> D[Test];
  B -- No --> E[Test];
  D ----> F[Test];
  E ----> F[Test];
  C ----> F[Test];
```
