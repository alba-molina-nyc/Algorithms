# Dictionaries AKA Associative Arrays

## Python's dictionaries

```python
d = {
    'name': 'Alba',
    'age': 28,
    'gender': female
}

print(d['name']) # returns Alba the value
print(d.items()) # return all the k,v pair
print(d.values())
print(d.keys())
```

### Iterate through dictionary

```python
for key, value in d.items():
    print(key, value)
```

---

## Dictionaries AKA Associative Arrays

- composd of a collection of `key-value-pairs` where each key appears at most once in the collection
- most of the times we implment associative arrays with a hashtable but binary search trees can be used as well
- the aim is to reach o(1) time complexity for most of the operations
