class Processor:
    """MOT-6502 Processor."""
    ...

    def fetch_byte(self) -> int:
        """Fetch a byte from memory.

        :param address: The address to read from
        :return: int
        """
        data = self.read_byte(self.program_counter)
        self.program_counter += 1
        return data


    def fetch_word(self) -> int:
        """Fetch a word from memory.

        :param address: The address to read from
        :return: int
        """
        data = self.read_word(self.program_counter)
        self.program_counter += 2
        return data
