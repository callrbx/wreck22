import time
import claripy
import angr
# coding: utf-8

# compiled on ubuntu 18.04 system:
# https://github.com/b01lers/b01lers-ctf-2020/tree/master/rev/100_little_no-peeking-dbg


def main():
    # setup of addresses used in program
    # addresses assume base address of
    base_addr = 0x100000

    # length of desired input is 75 as found from reversing the binary in ghidra
    # need to add 4 times this size, since the actual array is 4 times the size
    # 1 extra byte for first input
    input_len = 40

    # seting up the angr project
    # auto_load_libs can't be disabled as the test fails.
    p = angr.Project('./no-peeking-dbg',
                     main_opts={'base_addr': base_addr}, auto_load_libs=True)

    # looking at the code/binary, we can tell the input string is expected to fill 22 bytes,
    # thus the 8 byte symbolic size. Hopefully we can find the constraints the binary
    # expects during symbolic execution
    flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(input_len)]

    # extra \n for first input, then find the flag!
    flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])

    # enable unicorn no-peeking-dbg for fast efficient solving
    st = p.factory.full_init_state(
        args=['./no-peeking-dbg'],
        add_options=angr.options.unicorn,
        stdin=angr.SimFileStream(
            name='stdin', content=flag, has_end=False)
    )

    # constrain to non-newline bytes
    # constrain to ascii-only characters
    for k in flag_chars:
        st.solver.add(k < 0x7f)
        st.solver.add(k > 0x20)

    # Construct a SimulationManager to perform symbolic execution.
    # Step until there is nothing left to be stepped.
    sm = p.factory.simulation_manager(st)
    sm.run()

    # grab all finished states, that have the win function output in stdout
    for x in sm.deadended:
        if b"Submit" in x.posix.dumps(1):
            if b"flag{" in x.posix.dumps(0):
                print(x.posix.dumps(0))


if __name__ == "__main__":
    before = time.time()
    main()
    after = time.time()
    print("Time elapsed: {}".format(after - before))

# flag{n0_peeking!_really_i_m3an_it_72db8}
