import java.util.Scanner;

public class countNumberOfDigits {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scn = new Scanner(System.in);

		int n = scn.nextInt();
		int c = 0;

		while (n != 0) {
			n = n / 10;
			c++;
		}
		System.out.print(c);

		// print digits
		c = scn.nextInt();
		String s = String.valueOf(c);
		for (int i = 0; i < s.length(); i++) {
			System.out.println(s.charAt(i));
		}

	}

}
