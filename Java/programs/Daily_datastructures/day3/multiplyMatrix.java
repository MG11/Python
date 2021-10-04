import java.util.Scanner;

public class multiplyMatrix {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);

		int m1 = scn.nextInt();
		int m2 = scn.nextInt();
		System.out.print("Enter array");
		int m[][] = new int[m1][m2];
		for (int i = 0; i < m1; i++) {
			for (int j = 0; j < m2; j++) {
				m[i][j] = scn.nextInt();
			}
		}

		int n1 = scn.nextInt();
		int n2 = scn.nextInt();
		System.out.print("Enter array");
		int n[][] = new int[n1][n2];
		for (int i = 0; i < n1; i++) {
			for (int j = 0; j < n2; j++) {
				n[i][j] = scn.nextInt();
			}
		}

		if (m2 != n1) {
			System.out.print("invalid input");
			return;
		}

		int prod[][] = new int[m1][n2];

		for (int i = 0; i < m1; i++) {
			for (int j = 0; j < n2; j++) {

				int val = 0;
				for (int k = 0; k < m2; k++) {
					val += m[i][k] * n[k][j];
				}
				prod[i][j] = val;
			}
		}

		for (int i = 0; i < m1; i++) {
			for (int j = 0; j < n2; j++) {
				System.out.print(prod[i][j] + " ");
			}
			System.out.println();
		}

	}

}
