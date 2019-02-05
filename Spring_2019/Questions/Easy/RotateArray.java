import java.util.Arrays;

/**
 * @author Drew Mitchell, TTU-ACM (Applied Algorithms)
 * Problem Source: https://leetcode.com/problems/rotate-array/
 */

public class RotateArray {
	public static void main(String[] args) { //Example test case
		int[] input = new int[] {1,2,3,4,5,6,7};
		rotate(input, 3);
		System.out.println(Arrays.toString(input));
	}
	
	public static void rotate(int[] nums, int k) {
		int[] temp = Arrays.copyOf(nums, nums.length); //Make a copy as to preserve the original order of the deep copy passed into the method
		for(int i = 0; i < temp.length; i++) {
			int newPos = i+k;
			if(newPos >= temp.length) { //if the new position is outside the index range
				newPos %= temp.length; //take away any index range value worth of indices.
			}
			nums[newPos] = temp[i]; //Take the number that was originally at i and put it back at i+k, 3 steps ahead in the provided example
		}
	}
}