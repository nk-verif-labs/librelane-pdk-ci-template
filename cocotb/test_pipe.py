import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_smoke(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    dut.rst_n.value = 0; dut.s_valid.value = 0; dut.m_ready.value = 1; dut.s_data.value = 0
    for _ in range(3): await RisingEdge(dut.clk)
    dut.rst_n.value = 1; dut.s_valid.value = 1; dut.s_data.value = 0xA5
    await RisingEdge(dut.clk); await RisingEdge(dut.clk)
    assert int(dut.m_valid.value) == 1 and int(dut.m_data.value) == 0xA5
