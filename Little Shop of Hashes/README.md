# Little Shop of Hashes

1. What is the name of the service that the attacker ran and stopped, which dumped hashes on the first compromised host?
    - `% grep -rh running -B1 . | grep param1 | sort -u`
    - `Remote Registry` was the answer

2. What lateral movement technique did the threat actor use to move to the other machine?
    - `flag{Pass-the-Hash}`

3. What is the full path of the binary that the threat actor used to access the privileges of a different user with
   explicit credentials?
    - `C:\\Users\\DeeDee\\Documents\\runasc.exe`

4. How many accounts were compromised by the threat actor?
    - `3`

5. What is the full path of the binary that was used as a callback to the threat actor's machine?
    - `C:\Users\DeeDee\Documents\nc.exe`
