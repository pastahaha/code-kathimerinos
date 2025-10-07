class Solution {
    public String reverseWords(String s) {
        List<String> sent = new ArrayList<>();
        int i=0;
        int leng = s.length();
        while (i<leng){
            while((i<leng) && (s.charAt(i) == ' ')){
                i+=1;
            }
            if(i==leng){
                break;
            }

            StringBuilder word = new StringBuilder();
            while(i < leng && s.charAt(i)!= ' '){
                word.append(s.charAt(i));
                i+=1;
            }
            sent.add(word.toString());
        }
        Collections.reverse(sent);
        return String.join(" ", sent);
    }
}