import m6502


def test_cpu_ins_nop() -> None:
    """
    Do nothing for 1 computer cycle.

    return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    memory[0xFCE2] = 0xEA
    cpu.execute(2)
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
    ) == (0xFCE3, 0x01FD, 2)
