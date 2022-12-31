var rearrangeArray = function(nums) {
    let i=0
    while(i<nums.length-1){
        if(nums[i]==(nums[i-1]+nums[i+1])/2){
            temp=nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=temp
            if(i>1){
                i--
            }
        }
        else{
            i++
        }
  
    }
    return nums
};
