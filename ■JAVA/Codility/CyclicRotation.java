package com.company.codility;


public class CyclicRotation {
    public int[] solution(int[] A, int K) {
        int[] S = new int[A.length];
        for (int i = 0; i < A.length; i++){
            S[(i+K) % A.length] = A[i];
        }
        return S;
    }
}
