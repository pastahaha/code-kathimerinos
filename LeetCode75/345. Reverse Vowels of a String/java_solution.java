class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int i=0, leng=chars.length-1;
        HashSet<Character> vowels = new HashSet<>();
        String vowelsS="aeiouAEIOU";
        char[] vow = vowelsS.toCharArray();
        for (int x=0; x<vow.length;x++){
            vowels.add(vow[x]);
        }
        while (i<leng){
            if ((vowels.contains(chars[i])) && (vowels.contains(chars[leng]))){
                char temp = chars[i];
                chars[i] = chars[leng];
                chars[leng] = temp;
                i+=1;
                leng-=1;
            }
            if(!vowels.contains(chars[i])){
                i+=1;
            }
            if(!vowels.contains(chars[leng])){
                leng-=1;
            }
        }
        return new String(chars);
    }
}