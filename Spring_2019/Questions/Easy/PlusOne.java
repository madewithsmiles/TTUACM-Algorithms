import java.util.Arrays;

/**
 * @author Drew Mitchell, TTU-ACM (Applied Algorithms)
 * Problem Source: https://leetcode.com/problems/plus-one/
 */

public class PlusOne {
	
	//This was just my attempt at the solution. It's robust, but not entirely pretty.
	public int[] plusOne(int[] digits) {
        int addCarry = 1; //Initial value is 1 as given by the problem; we want to add 1 to the ones place.
        for(int i = digits.length - 1; i >= 0; i--) { //Start from the right, since it's our least significant digit and thus what we should add one to.
            int currentPlace = digits[i]; //Observe the value of the place we're at.
            if(addCarry > 0) { //
                currentPlace += addCarry;
                addCarry = -1; //Reset the carry flag so that it will be ignored next loop.
            }
            if(currentPlace >= 10) { //Do we need to carry some digits to the next significant place?
                addCarry = currentPlace / 10; //Set the carry flag to add it to the next higher place during our next loop.
                currentPlace %= 10; //Get your remainder, i.e. ones value for the place we're on right now.
                if(i == 0) { //Is this the final time we will be looping?
                    int[] oldDig = Arrays.copyOf(digits, digits.length); //We need to add a number place at the very beginning for our carry.
                    digits = new int[oldDig.length+1];
                    for(int j = 1; j < oldDig.length; j++) digits[j] = currentPlace; //Add all values into the lower number places, leaving the most significant one at the default 0.
                    i++; //Ensure we run the loop one final time.
                    continue;
                }
            }
            digits[i] = currentPlace; //Finally modify the number place we were looking at.
        }
        return digits;
    }
}