class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        for(int x=0; x< candies.length; x++){
            int curr=candies[x]+extraCandies;
            result.add(checkMax(curr, candies));
        }
        return result;
    }

    private Boolean checkMax(int curr, int[] candies){
        for(int x=0; x< candies.length; x++){
            if (curr < candies[x]){
                return false;
            }
        }
        return true;
    }
}
