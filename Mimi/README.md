# Mimi

It is a dump of memory from `lsass.exe`. It can be extracted using MimiKatz or using `pypykatz`:

```shell
% pypykatz lsa minidump mimi.dmp | grep 'flag{'`
```