# LibreLane PDK + Cocotb CI Template (IHP SG13G2)
[[https://github.com/nk-verif-labs/librelane-pdk-ci-template/actions/workflows/ci.yml/badge.svg]](https://github.com/nk-verif-labs/librelane-pdk-ci-template/actions/workflows/ci.yml)

Reusable RTL-to-GDSII + RTL & post-PnR Gate-Level Cocotb template for **IHP SG13G2** using Nix + LibreLane.

## Quick Start
    nix develop --command make clone-pdk && nix develop --command make sim && nix develop --command make librelane-nodrc && nix develop --command make sim-gl
