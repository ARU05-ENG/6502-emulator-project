def test_cpu_fetch_byte() -> None:
    """Verify CPU can fetch a byte from memory.

    The cost of the fetch operation is 1 cycle, and increases the
    program counter by 1. The state of the CPU is not changed
    further.

    :return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    memory[0xFCE2] = 0xA5
    value = cpu.fetch_byte()
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
        value,
    ) == (0xFCE3, 0x01FD, 1, True, False, True, 0xA5)

def test_cpu_fetch_word() -> None:
    """Verify CPU can fetch a word from memory.

    The cost of the fetch operation is 2 cycle, and increases the
    program counter by 2. The state of the CPU is not changed
    further.

    :return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    memory[0xFCE2] = 0xA5
    memory[0xFCE3] = 0x5A
    value = cpu.fetch_word()
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
        value,
    ) == (0xFCE4, 0x01FD, 2, True, False, True, 0x5AA5)
