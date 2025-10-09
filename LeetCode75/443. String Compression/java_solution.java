class Solution {
    public int compress(char[] chars) {
        int left=0;
        int right=0;
        int leng=chars.length;

        while(right<leng){
            char curr = chars[right];
            int count = 0;

            while(right<leng && chars[right]==curr){
                right++;
                count++;
            }

            chars[left]=curr;
            left++;

            if(count>1){
                String countString=String.valueOf(count);
                for(int i=0; i<countString.length();i++){
                    chars[left]=countString.charAt(i);
                    left++;
                }

            }
        }
        return left;
    }
}