/**
* Author: Drew Mitchell
* Date: 10/26/2018
* Description: A basical functional algorithm that will progress procedurally through a string and output a substring
* specified by given parameters; the idea is that the program will loop the string infinitely as on a vertically-limited display sign.
*/

public class ScrollString
{
	public static void main(String[] args) {
		int length = 10;
		int padding = 2;
		String pt = "Welcome to the AMAZING world of Jurassic Park!";
		int iterations = pt.length() + 15; //Could be run infinitely asynchronous, this number is basically a limiting factor to make sure it's not an infinite loop
		for (int i = 0; i < iterations; i++) {
			System.out.println(scrollString(pt, length, padding, i)); //The default output channel chosen is sysout, but could very well be some text display field that is updated occasionally
		}
	}
	
	public static String scrollString(String orig, int length, int spaceBetween, int startIndex) {
		int endIndex = startIndex + length;
		String s;
		if(startIndex + length > orig.length()) {
			if(startIndex > orig.length()) {
				s = "";
				int defecit = startIndex - orig.length();
				if(s.equals(" " + orig.substring(0, length - 1))) startIndex = 0;
				while(defecit > 0) {
					s += " ";
					defecit--;
				}
				if(s.length() < length) s += orig.substring(0, length - s.length());
				return s;
			}
			s = orig.substring(startIndex, orig.length());
			if((endIndex - orig.length()) > 0) {
				while((endIndex - orig.length()) > 0) {
					if(spaceBetween > 0) {
						s += " ";
						endIndex--;
						spaceBetween--;
					}
					else break;
				}
				while(s.length() < length) {
					s += " ";
				}
			}
			if((endIndex - orig.length()) < 0) {
				s = "";
				while((endIndex - orig.length()) < 0) {
					if(spaceBetween > 0) {
						s += " ";
						endIndex--;
						spaceBetween--;
					}
					else break;
				}
				while(s.length() < length) {
					s += orig.substring(endIndex, endIndex + 1);
					endIndex++;
				}
			}
			return s;
		}
		return orig.substring(startIndex, (startIndex + length));
	}
}
