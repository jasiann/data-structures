# Python data structures 

## What's in the Repository 

- Hashtable: Stores key-value pairs using hashing. 
- DynamicArray: a resizable array that supports adding, removing, and accessing elements 
- Stack: last-in-first-out (LIFO) stack backed by a Python list; top = end of the list.

## Running Tests: 

Run the following command: 

python3 -m pytest 

## Time Complexity

| Structure    | Operation       | Average   | Worst | Why |
|--------------|-----------------|-----------|-------|-----|
| HashTable    | get/put/delete  | O(1)      | O(n)  | Even hash distribution → ~constant per bucket; all keys collide → linear scan. |
| HashTable    | resize          | O(1) amort| O(n)  | One resize rehashes all n elements; doubling spreads cost → O(1) amortized. |
| DynamicArray | append          | O(1) amort| O(n)  | Write at end is O(1); full capacity → copy all n elements, geometric growth amortizes. |
| DynamicArray | get by index    | O(1)      | O(1)  | Direct address arithmetic: base + index * element_size. |
| Stack        | push            | O(1) amort| O(n)  | list.append at the end; when the list's capacity is full, Python copies to a bigger array (same as DynamicArray). |
| Stack        | pop / peek      | O(1)      | O(1)  | Top is the last element; index -1 gives direct O(1) access. |

