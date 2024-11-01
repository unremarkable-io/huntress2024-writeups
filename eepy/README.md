# eepy

At `0x140003020` there is a buffer of 38 bytes that contains the flag XORed with `0xAA`, decode like this, voila!

```shell
% r.emit 'CCC6CBCDD198CCCFC899CCCC92CB989BCB999CCEC89BCBCE99929CCE9999CB9893CE929FCBD7' | r.hex | r.xor h:aa   
flag{2feb3ff8a21a36db1ad386d33a29d85a}
```
