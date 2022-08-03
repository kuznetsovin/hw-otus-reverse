#!/usr/bin/env python3
from capstone import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command opcode generator')
    parser.add_argument('max_size', type=int, help='max command size in bytes')

    args = parser.parse_args()
    max_cmd_size = args.max_size

    cs = Cs(CS_ARCH_X86, CS_MODE_16)

    results = {}
    for i in range(0, pow(2, max_cmd_size * 8)):
        # generate byte sequence
        code = i.to_bytes(max_cmd_size, byteorder="little")
        # tranform sequence of bytes to asm code
        disasm_code = list(cs.disasm(code, 0x00))
        if len(disasm_code) > 0:
            # get first asm instruction
            res = format("%s %s" % (disasm_code[0].mnemonic, disasm_code[0].op_str))

            # if this is new instruction, then init set of opcodes for it
            if not res in results:
                results[res] = set()

            # add finding opcodes to the set of instruction opcodes
            results[res].add(disasm_code[0].bytes.hex())

    # save result to file
    with open('results.txt', 'w') as f:
        for k, v in results.items():
            if len(v) > 1:
                f.write(format("%s: %s\n" % (k, v)))
