# VerilogCodeGenerator
在写 verilog 汇编代码时往往很多内容都是重复的，它们仅仅是 pin 编号不同,本脚本提供这种代码的一键生成。

例如：

```verilog
FullAdder	fir1fa1( pp0[2], pp1[1], pp2[0], Fir1_S[1], Fir1_C[1] );
FullAdder	fir1fa2( pp0[3], pp1[2], pp2[1], Fir1_S[2], Fir1_C[2] );
FullAdder	fir1fa3( pp0[4], pp1[3], pp2[2], Fir1_S[3], Fir1_C[3] );
FullAdder	fir1fa4( pp0[5], pp1[4], pp2[3], Fir1_S[4], Fir1_C[4] );
```

也可以作为一种模板，利用正则表达式扩充更加复杂的功能。
