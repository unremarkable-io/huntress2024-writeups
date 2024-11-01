# Ping Me

Run the VBS somewhere online without Execute, then in python:

```python
>>> bytes(map(int, '.'.join(["102.108.97.103", "123.54.100.49", "98.54.48.52", "98.98.49.98", "54.100.97.51", "50.98.56.98", "98.99.97.57", "101.50.54.100", "53.49.53.56", "57.125.35.35"]).split('.')))
b'flag{6d1b604bb1b6da32b8bbca9e26d51589}##'
```
