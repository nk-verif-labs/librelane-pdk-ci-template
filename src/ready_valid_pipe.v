`timescale 1ns/1ps
module ready_valid_pipe #(parameter WIDTH = 8) (
  input wire clk, input wire rst_n,
  input wire s_valid, output wire s_ready, input wire [WIDTH-1:0] s_data,
  output reg m_valid, input wire m_ready, output reg [WIDTH-1:0] m_data
);
  assign s_ready = !m_valid || m_ready;
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin m_valid <= 1'b0; m_data <= {WIDTH{1'b0}}; end
    else if (s_ready) begin m_valid <= s_valid; if (s_valid) m_data <= s_data; end
  end
endmodule
