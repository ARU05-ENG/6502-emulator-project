class Processor:
    """MOT-6502 Processor."""
    ...

    def execute(self, cycles: int = 0) -> None:
        """
        Execute code for X amount of cycles. Or until a breakpoint is reached.

        :param cycles: The number of cycles to execute
        :return: None
        """
        while (self.cycles < cycles) or (cycles == 0):
            opcode = self.fetch_byte()
            if opcode == 0x18:
                self.ins_nop_imp()
            elif opcode == 0xEA:
                self.ins_clc_imp()
            ...

    def ins_nop_imp(self) -> None:
        """
        NOP - No Operation.

        :return: None
        """
        self.cycles += 1

    def ins_clc_imp(self) -> None:
        """
        CLC - Clear Carry Flag.

        :return: None
        """
        self.flag_c = False
        self.cycles += 1
