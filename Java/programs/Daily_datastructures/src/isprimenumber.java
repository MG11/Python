import java.util.Scanner;

public class isprimenumber {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);

		// write ur code here
		int t = scn.nextInt();

		for (int i = 0; i < t; i++) {
			int n = scn.nextInt();
			if (checkprime2(n)) {
				System.out.println("prime");
			} else {
				System.out.println("not prime");
			}
//			checkprime2(n);
		}

	}

	// O(n) / O(n)
	public static boolean checkprime(int n, int start) {
		if (n == 1) {
			return false;
		}

		if (n == start) {
			return true;
		}

		if (n % start == 0) {
			return false;
		}

		start += 1;
		return checkprime(n, start);
	}

	// O(sqrt(n))/ O(1)
	public static boolean checkprime2(int n) {
		boolean isPrime = true;
		for (int i = 2; i * i <= n; i++) {
			if (n % i == 0) {
				isPrime = false;
				break;
			}
		}
		return isPrime;

	}
}
