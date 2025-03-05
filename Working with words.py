class Processor:
    """MOT-6502 Processor."""
    ...

    def read_word(self, address: int) -> int:
        """Read a word from memory.

        :param address: The address to read from
        :return: int
        """
        if sys.byteorder == "little":
            data = self.read_byte(address) | (self.read_byte(address + 1) << 8)
        else:
            data = (self.read_byte(address) << 8) | self.read_byte(address + 1)
        return data


    def write_word(self, address: int, value: int) -> None:
        """Split a word to two bytes and write to memory.

        :param address: The address to write to
        :param value: The value to write
        :return: None
        """
        if sys.byteorder == "little":
            self.write_byte(address, value & 0xFF)
            self.write_byte(address + 1, (value >> 8) & 0xFF)
        else:
            self.write_byte(address, (value >> 8) & 0xFF)
            self.write_byte(address + 1, value & 0xFF)
def test_cpu_read_write_word() -> None:
    """Verify CPU can read and write a byte from memory.

    The cost of the read and write operation is 2 cycles each, and
    the state of the CPU is not changed.

    :return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    cpu.write_word(0x0001, 0x5AA5)
    value = cpu.read_word(0x0001)
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
        value,
    ) == (0xFCE2, 0x01FD, 4, True, False, True, 0x5AA5)
