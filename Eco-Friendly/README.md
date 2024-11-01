# Eco-Friendly

agentzulu has a nicer/simpler solution than we did using PowerShell ISE (less manually mess):

Open it in PowerShell ISE, set a breakpoint on the line (takes a long time it is 7MB). Then step into until you reach
the last layer (it is stacked again and again ...):

```powershell
iex ('{39}{23}{26}{13}{21}{16}{17}{14}{27}{9}{22}{3}{12}{1}{5}{20}{8}{38}{37}{7}{30}{6}{34}{11}{18}{4}{36}{19}{0}{24}{28}{32}{40}{35}{31}{25}{29}{33}{2}{15}{10}' -f [char]55,$env:ComSpec[22],[char]54,[char]52,$env:PUBLiC[11],$env:ProgramFiles[14],[char]56,[char]53,$env:ComSpec[15],$env:PUBLiC[11],[char]125,$env:Comspec[22],$env:Comspec[17],[char]102,[char]123,$env:Comspec[17],$env:ProgramFiles[8],$env:CommonProgramFiles[6],$env:PUBLiC[11],[char]55,[char]49,$env:ProgramFiles[13],$env:ProgramData[11],[char]35,$env:Comspec[18],$env:ComSpec[17],$env:CommonProgramFiles[10],[char]56,$env:Comspec[18],[char]57,$env:Comspec[18],$env:Comspec[18],$env:PUBLiC[5],$env:CommonProgramW6432[8],[char]55,[char]49,[char]102,[char]57,[char]48,$env:CommonProgramW6432[23],[char]53)
```

Just change iex to Write-Output in a new script.

flag{8ba43de1e095287dbbf7722e51239a63}
