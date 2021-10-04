import java.util.Scanner;

public class numberSystem {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int d = scn.nextInt();

		int numberConverted = decimalToAnyBase(n, d);
		System.out.println(numberConverted);

		numberConverted = anyBaseToDecimal(n, d);
		System.out.println(numberConverted);

		numberConverted = sumNumbersOfAnyBase(534, 467, 8);
		System.out.println(numberConverted);

	}

	public static int sumNumbersOfAnyBase(int n1, int n2, int b) {
		int sum = 0;
		int pos = 1;
		int c = 0;
		while (n1 > 0 || n2 > 0 || c > 0) {
			int d = n1 % 10;
			int m = n2 % 10;
			n1 = n1 / 10;
			n2 = n2 / 10;
			int digit = d + m + c;
			if (digit >= b) {
				c = 1;
				digit = digit - b;
			} else {
				c = 0;
			}
			sum = sum + (digit) * pos;
			pos = pos * 10;
		}
		return sum;
	}

	public static int anyBaseToDecimal(int n, int d) {
		int converted = 0;
		int pos = 1;
		while (n != 0) {
			int rem = n % 10;
			n = n / 10;
			converted = converted + rem * pos;
			pos = pos * d;
		}
		return converted;
	}

	public static int decimalToAnyBase(int n, int d) {
		int converted = 0;
		int position = 1;
		while (n != 0) {
			int r = n % d;
			n = n / d;
			converted = converted + position * r;
			position = position * 10;
		}

		return converted;
	}

}
