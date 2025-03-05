class Processor:
    """MOT-6502 Processor."""
    ...

    def read_byte(self, address: int) -> int:
        """Read a byte from memory.

        :param address: The address to read from
        :return: int
        """
        data = self.memory[address]
        self.cycles += 1
        return data


    def write_byte(self, address: int, value: int) -> None:
        """Write a byte to memory.

        :param address: The address to write to
        :param value: The value to write
        :return: None
        """
        self.memory[address] = value
        self.cycles += 1
def test_cpu_read_write_byte() -> None:
    """Verify CPU can read and write a byte from memory.

    The cost of the read and write operation is 1 cycle each, and
    the state of the CPU is not changed.

    :return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    cpu.write_byte(0x0001, 0xA5)
    value = cpu.read_byte(0x0001)
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
        value,
    ) == (0xFCE2, 0x01FD, 2, True, False, True, 0xA5)
