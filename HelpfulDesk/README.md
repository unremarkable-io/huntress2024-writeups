# HelpfulDesk

A challenge previously used in NahamCon 2024, there is even a write-up from the author:
 - https://web.archive.org/web/20240612211647/https://notes.huskyhacks.dev/blog/helpfuldesk-walkthrough-nahamcon-2024-ctf

Diff the `helpfuldesk.dll` between version v1.1 and v1.2 and find the modified line:

```csharp
string requestPath = base.HttpContext.Request.Path.Value; // v1.1
string requestPath = base.HttpContext.Request.Path.Value.TrimEnd('/'); // v1.2

if (requestPath.Equals("/Setup/SetupWizard", StringComparison.OrdinalIgnoreCase))
{
    return this.View("Error", new ErrorViewModel
    {
        RequestId = "Server already set up.",
        ExceptionMessage = "Server already set up.",
        StatusCode = 403
    });
}
```

Exploitation:

Browse to `/Setup/SetupWizard/`, reset the password for admin, login, download flag.txt from the first computer.
