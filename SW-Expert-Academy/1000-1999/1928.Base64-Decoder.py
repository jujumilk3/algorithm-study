baseAZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
base = {i: ord(i) - 65 for i in baseAZ}
for a in baseAZ.lower():
    base[a] = ord(a) - 71
for n in range(0, 10):
    base[str(n)] = ord(str(n)) + 4
base["+"] = 62
base["/"] = 63

T = int(input())
for i in range(1, T + 1):
    bit = input()
    result = ""
    for j in range(0, len(bit), 4):
        temp = ""
        for k in bit[j:j + 4]:
            temp += format(base[k], 'b').zfill(6)
        for m in range(0, len(temp), 8):
            result += chr(int(temp[m:m + 8], 2))
    print(f"#{i}", result)

"""
10
TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
U3VzcGljaW9uIGZvbGxvd3MgY2xvc2Ugb24gbWlzdHJ1c3Qu
VG8gZG91YnQgaXMgc2FmZXIgdGhhbiB0byBiZSBzZWN1cmUu
T25seSB0aGUganVzdCBtYW4gZW5qb3lzIHBlYWNlIG9mIG1pbmQu
QSBmdWxsIGJlbGx5IGlzIHRoZSBtb3RoZXIgb2YgYWxsIGV2aWwu
QSBnaWZ0IGluIHNlYXNvbiBpcyBhIGRvdWJsZSBmYXZvciB0byB0aGUgbmVlZHku
Qm9va3MgYXJlIHNoaXBzIHdoaWNoIHBhc3MgdGhyb3VnaCB0aGUgdmFzdCBzZWFzIG9mIHRpbWUu
TGV0IHRoeSBzcGVlY2ggYmUgc2hvcnQsIGNvbXByZWhlbmRpbmcgbXVjaCBpbiBmZXcgd29yZHMu
VGhlIHdvcmxkIGlzIGEgYmVhdXRpZnVsIGJvb2ssIGJ1dCBvZiBsaXR0bGUgdXNlIHRvIGhpbSB3aG8gY2Fubm90IHJlYWQgaXQu
SGUgd2hvIHNwYXJlcyB0aGUgcm9kIGhhdGVzIGhpcyBzb24sIGJ1dCBoZSB3aG8gbG92ZXMgaGltIGlzIGNhcmVmdWwgdG8gZGlzY2lwbGluZSBoaW0u
"""
