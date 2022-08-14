# Linked Lists

## How Linked Lists came about

Arrays have a huge disadvantage: there are many _holes_ in the data structure and we have to shift a lot of the time

for example, if we want to insert an item in the middle of the list or even the beginning, we need to shift everything to the right once we make those insertions

```python
list = [1, 2, 3]
```

if you want to insert 25 at index 1, then values at index 1 and index 2 also have to be shifted to the right.

```python
list = [1, 25, 2, 3]
```

`Linked Lists` allows to store items more efficiently than arrays/lists especially when it comes to `insertion` and `removal operations`

---

## About Linked Lists

- every node stores the data and a reference to the next node in the linked list data structure
  - this is why **linked lists** require more memory than arrays
- but the advantage is that you do not need to shift items!

---