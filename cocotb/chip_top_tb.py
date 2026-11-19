import glob, os
from pathlib import Path
from cocotb_tools.runner import get_runner

root = Path(__file__).resolve().parent.parent
gl = os.getenv("GL") == "1"
sources = [root / "src" / "ready_valid_pipe.v"]
defines = {}
if gl:
    pdk_root = os.environ["PDK_ROOT"]
    pdk = os.getenv("PDK", "ihp-sg13g2")
    sources = [root / "final" / "nl" / "ready_valid_pipe.nl.v"] + sorted(
        Path(p) for p in glob.glob(f"{pdk_root}/{pdk}/libs.ref/sg13g2_stdcell/verilog/*.v")
    )
    defines = {"FUNCTIONAL": 1, "UNIT_DELAY": "#0"}
runner = get_runner("icarus")
runner.build(sources=sources, hdl_toplevel="ready_valid_pipe", defines=defines, build_dir=root / "cocotb" / "sim_build", always=True)
runner.test(hdl_toplevel="ready_valid_pipe", test_module="test_pipe", build_dir=root / "cocotb" / "sim_build")
