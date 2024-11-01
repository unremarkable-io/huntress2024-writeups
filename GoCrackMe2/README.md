# GoCrackMe2

It prints parts of the flag as a random number controls the code flow - that can be removed by patching the binary.

NOP out the stuff from `0x4881A3` through to `0x4881A9`, it should look like this after:

```
.text:000000000048819F                 ucomisd xmm1, xmm0
.text:00000000004881A3                 nop
.text:00000000004881A4                 nop
.text:00000000004881A5                 nop
.text:00000000004881A6                 nop
.text:00000000004881A7                 nop
.text:00000000004881A8                 nop
.text:00000000004881A9                 nop
.text:00000000004881AA                 lea     rax, RTYPE_uint8
```
