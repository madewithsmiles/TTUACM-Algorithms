import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class BasicMathAlgorithms
{
	public static void main(String[] args) {
		System.out.print("Enter the quantity of random numbers:  ");
		Scanner scan = new Scanner(System.in);
		int listSize = scan.nextInt();
		System.out.println();
		Statistics intList = new Statistics(listSize);
		intList.randomize();
		intList.computeMean();
		intList.computeMedian();
		intList.computeMode();
		intList.displayStats();
		scan.close();
	}
}

class Statistics {
	private int list[];
	private int size;
	private double mean;
	private double median;
	private int mode;

	public Statistics(int s) {
		size = s;
		list = new int[size];
		mean = median = mode = 0;
	}
	
	public void randomize()
	{
		Random rand = new Random(12345);
		for (int k = 0; k < size; k++)
		    list[k] = rand.nextInt(31) + 1;  // range of 1..31
	}

	
	public void computeMean() {
		int sum = 0;
		for(int i : list) {
			sum += i;
		}
		System.out.println(sum);
		mean = (double) sum / size;
	}
	
	public void computeMedian() {
		Arrays.sort(list);
		if(size % 2 == 1) {
			//If it's odd
			int middle = list[(int) Math.round((double) (size - 1) / 2)];
			median = middle;
		}
		else {
			int middle1 = list[(size / 2) - 1];
			int middle2 = list[size / 2];
			median = ((double) middle1 + middle2) / 2;
		}
	}
	
	public void computeMode() {
		int prevNumber = 0;
		int occurances = 0;
		int mostOccurances = 0;
		int mostOccuredNum = 0;
		for(int i = 0; i < list.length; i++) {
			if(list[i] != prevNumber) { //If this next number isn't the one we were tracking
				if(mostOccurances <= occurances) { //If the one we were tracking is the bigger dog than the one before it
					mostOccurances = occurances;
					mostOccuredNum = prevNumber;
				}
				prevNumber = list[i]; //Reset the data to the newly tracked number
				occurances = 0;
			}
			else occurances++;
		}
		mode = mostOccuredNum;
	}
	
	public void displayStats() {
		System.out.println("\n" + Arrays.toString(list) + "\n");
		System.out.println("Mean:    " + mean);
		System.out.println("Median:  " + median);
		System.out.println("Mode:    " + mode + "\n");
	}
}