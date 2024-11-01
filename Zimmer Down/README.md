# Zimmer Down

Using [regrip.py](https://github.com/airbus-cert/regrippy) I was able to extract data from `NTUSER.DAT`:

```shell
% regrip.py --ntuser NTUSER.DAT recentdocs
```

One of them was `VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF.b62` - that is the flag in Base62 encoding.

You can decode it e.g. using [Binary Refinery](https://github.com/binref/refinery):

```shell
% r.emit VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF | r.base 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```