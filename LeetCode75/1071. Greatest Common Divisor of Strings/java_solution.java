class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(str1 == null || str2 == null){
            return "";
        }
        if(str1.length() == 0 || str2.length() == 0){
            return "";
        }
        if(!(str1+str2).equals(str2+str1)){
            return "";
        }
        int x = gcd(str1.length(),str2.length());
        return str1.substring(0,x);
    }
    private int gcd(int num1, int num2){
        while(num2!=0){
            int temp = num2;
            num2=num1%num2;
            num1=temp;
        }
        return num1;
    }
}