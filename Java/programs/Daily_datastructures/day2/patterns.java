import java.util.Scanner;

public class patterns {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scn = new Scanner(System.in);

		// write your code here

//		1
//		1	1
//		1	2	1
//		1	3	3	1
//		1	4	6	4	1

		int n = scn.nextInt();

		for (int i = 0; i <= n; i++) {
			int val = 1;
			for (int j = 0; j <= i; j++) {
				System.out.print(val + "\t");
				val = val * (i - j) / (j + 1);
			}
			System.out.println();
		}
//
//			1
//		2	3	2
//	3	4	5	4	3
//		2	3	2
//			1

		int space = n / 2;
		int stars = 1;
		int val = 1;
		for (int i = 1; i <= n; i++) {
			int ival = val;
			for (int j = 1; j <= space; j++) {
				System.out.print(" ");
			}
			for (int j = 1; j <= stars; j++) {
				System.out.print(ival);
				if (j <= stars / 2) {
					ival++;
				} else {
					ival--;
				}
			}
			System.out.println();
			if (i <= n / 2) {
				space--;
				stars += 2;
				val++;
			} else {
				space++;
				stars -= 2;
				val--;
			}
		}

//		1												1
//		1	2										2	1
//		1	2	3								3	2	1
//		1	2	3	4						4	3	2	1
//		1	2	3	4	5				5	4	3	2	1
//		1	2	3	4	5	6		6	5	4	3	2	1
//		1	2	3	4	5	6	7	6	5	4	3	2	1

		space = 2 * n - 3;

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.print(j);
			}
			for (int j = 1; j <= space; j++) {
				System.out.print(" ");
			}
			for (int j = i; j >= 1; j--) {
				if (j == n) {
					continue;
				}
				System.out.print(j);
			}
			space -= 2;
			System.out.println();
		}

	}

}
