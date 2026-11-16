# Python data structures 

## What's in the Repository 

- Hashtable: Stores key-value pairs using hashing. 
- DynamicArray: a resizable array that supports adding, removing, and accessing elements 

## Running Tests: 

Run the following command: 

python 3 -m pytest 

## Time Complexity

| Structure    | Operation       | Average   | Worst | Why |
|--------------|-----------------|-----------|-------|-----|
| HashTable    | get/put/delete  | O(1)      | O(n)  | Even hash distribution → ~constant per bucket; all keys collide → linear scan. |
| HashTable    | resize          | O(1) amort| O(n)  | One resize rehashes all n elements; doubling spreads cost → O(1) amortized. |
| DynamicArray | append          | O(1) amort| O(n)  | Write at end is O(1); full capacity → copy all n elements, geometric growth amortizes. |
| DynamicArray | get by index    | O(1)      | O(1)  | Direct address arithmetic: base + index * element_size. |


