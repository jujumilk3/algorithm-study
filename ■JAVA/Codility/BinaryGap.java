package com.company.codility;

import java.util.*;

public class BinaryGap {
    public int solution(int N) {
        String binaryInteger = Integer.toBinaryString(N);
        ArrayList<Integer> founds = new ArrayList<>();
        int straight = 0;
        for (int i = 0; i < binaryInteger.length(); i++){
            if (binaryInteger.charAt(i) == '0'){
                straight++;
            }else if (straight != 0 && binaryInteger.charAt(i) == '1'){
                founds.add(straight);
                straight = 0;
            }
        }
        if (founds.isEmpty()){
            return 0;
        }else{
            return Collections.max(founds);
        }
    }
}
