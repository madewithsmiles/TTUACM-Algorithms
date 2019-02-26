public class Solution {
    /**
     * Medium level problem
     *
     * We should realize that a rotated array is just
     * nums[k -> end] + nums[0 -> k]
     *
     * Doing some reversing magic, we are able to reverse in place and in O(n)
     *
     * This problem helps you see that your problem should be broken down into
     * smaller problems. This is crucial for interviews and they want to see how
     * you break down really big problems. This will also be useful when we get to
     * graphs later in the semester
     */
    public void rotate(int[] nums, int k) {
        k %= nums.length; // At some point in time, we are doing more work than we need to
        reverse(nums, 0, nums.length - 1); // Reverse the entire array
        reverse(nums, 0, k - 1); // Reverse the first k items in the reversed array
        reverse(nums, k, nums.length - 1); // Reverse the k to last item in the array
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
