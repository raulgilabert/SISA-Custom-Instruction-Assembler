.text
movi r0, 0x00
movhi r0, 0x11
mvrv v0, r0, 0

movi r0, 0x22
movhi r0, 0x33
mvrv v0, r0, 1

movi r0, 0x44
movhi r0, 0x55
mvrv v0, r0, 2

movi r0, 0x66
movhi r0, 0x77
mvrv v0, r0, 3

movi r0, 0x88
movhi r0, 0x99
mvrv v0, r0, 4

movi r0, 0xaa
movhi r0, 0xbb
mvrv v0, r0, 5

movi r0, 0xcc
movhi r0, 0xdd
mvrv v0, r0, 6

movi r0, 0xee
movhi r0, 0xff
mvrv v0, r0, 7

movi r0, 0x00
movhi r0, 0x11
mvrv v1, r0, 0

movi r0, 0x22
movhi r0, 0x33
mvrv v1, r0, 1

movi r0, 0x44
movhi r0, 0x55
mvrv v1, r0, 2

movi r0, 0x66
movhi r0, 0x77
mvrv v1, r0, 3

movi r0, 0x88
movhi r0, 0x99
mvrv v1, r0, 4

movi r0, 0xaa
movhi r0, 0xbb
mvrv v1, r0, 5

movi r0, 0xcc
movhi r0, 0xdd
mvrv v1, r0, 6

movi r0, 0xee
movhi r0, 0xff
mvrv v1, r0, 7

addv v2, v0, v1

movi r1, 0x00
movhi r1, 0x00

STV 0(r1), v2
LDV v2, 0(r1)

halt

