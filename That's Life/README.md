# That's Life

The Go binary utilizes ProtoBuf to store game state.

Install `protodump` and extract the `.proto` files from the embedded metadata.

```shell
% go install github.com/arkadiyt/protodump/cmd/protodump@latest

% ~/go/bin/protodump -file gameoflife -output dumped
Wrote dumped/github.com/HuskyHacks/thats_life/pb/gameoflife.proto
```

Use `protoc` compiler to create Python bindings for the Protobuf:

```shell
% mv dumped/github.com/HuskyHacks/thats_life/pb/gameoflife.proto ./
% ./protoc --python_out=gameoflife_protobuf --pyi_out=gameoflife_protobuf gameoflife.proto
```

After discovering WinCriteria at `0x5F8538` / `0x1F8538` file offset and assigning the right type to it
(`main_WinCriteria`) all that was left was to write a script to generate the winning grid
([`thats_life.py`](thats_life.py)).

You can decode the generate `win_grid.pb` like this to check if it is correct (helpful for development):

```shell
% ./protoc --decode=thats_life.Grid ./gameoflife.proto < win_grid.pb
```
