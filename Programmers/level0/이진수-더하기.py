def solution(bin1, bin2):
    return bin(eval(f"0b{bin1} + 0b{bin2}")).replace("0b", "")
