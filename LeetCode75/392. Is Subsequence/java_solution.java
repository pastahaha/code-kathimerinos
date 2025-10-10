class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s==null || s.isEmpty()){
            return true;
        }
        int i=0;
        int curr=0;

        while(curr<s.length() && i<t.length()){
            if(t.charAt(i)==s.charAt(curr)){
                curr++;
            }
            i++;
        }
        return (curr==s.length())?true:false;
    }
}