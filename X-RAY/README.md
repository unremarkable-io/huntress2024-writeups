# X-RAY

Found https://github.com/zam89/Windows-Defender-Quarantine-File-Decryptor, used it to decrypt the quarantined
file:

```shell
.\defender_file_decryptor.exe ..\x-ray ..\x-ray.decrypted
```

It is a .NET assembly, in dotPeek or anything else I noticed a string being decoded that was unused in the code:

```csharp
Encoding.UTF8.GetString(
StageTwo.otp(
StageTwo.load("15b279d8c0fdbd7d4a8eea255876a0fd189f4fafd4f4124dafae47cb20a447308e3f77995d3c"),
StageTwo.load("73de18bfbb99db4f7cbed3156d40959e7aac7d96b29071759c9b70fb18947000be5d41ab6c41")
)
);
```

- [`x-ray.py`](x-ray.py) to quickly XOR them together to get the flag

or using [Binary Refinery](https://github.com/binref/refinery):

```shell
% r.emit 15b279d8c0fdbd7d4a8eea255876a0fd189f4fafd4f4124dafae47cb20a447308e3f77995d3c | r.hex | r.xor h:73de18bfbb99db4f7cbed3156d40959e7aac7d96b29071759c9b70fb18947000be5d41ab6c41
flag{df26090565cb329fdc8357080700b621}
```
