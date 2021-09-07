package com.company.codility;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class OddOccurrencesInArray {
    public String solution(String S, String C) {
        System.out.println(S);
        System.out.println("###");
        System.out.println(C);
        String[] teamNames = S.split(",");
        String[] arrangedTeamNames = new String[teamNames.length];
        String[] emailList = new String[]{};
        for (String name: teamNames){
            String[] nameElements = name.trim().split(" ");
            System.out.println(Arrays.toString(nameElements));
            for (int i = 0; i < nameElements.length; i++){
                System.out.println(nameElements[i]);
            }
        }
        Arrays.toString(teamNames);
        Map.Entry
        return "TEST";
    }
}
