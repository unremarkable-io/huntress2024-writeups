#!/usr/bin/env python3
from pathlib import Path

import angr

project = angr.Project(Path(__file__).parent.joinpath('stack_it.bin'), auto_load_libs=False)


@project.hook(0x804904C)  # post flag decoding into memory
def post_flag_decode(state):
    flag_addr_in_memory = 0x0804A050
    data = state.solver.eval(state.memory.load(flag_addr_in_memory, 100), cast_to=bytes).rstrip(b'\x00')
    print('\npost_flag_decode', data)
    # project.terminate_execution()


@project.hook(0x8049052)  # post flag decoding, pointer in EDX
def post_flag_decode_via_register(state):
    data = state.solver.eval(state.memory.load(state.regs.edx, 100), cast_to=bytes).rstrip(b'\x00')
    print('\npost_flag_decode_via_register', data)
    project.terminate_execution()  # terminate is here as it is later than post_flag_decode()


project.execute()
print()
