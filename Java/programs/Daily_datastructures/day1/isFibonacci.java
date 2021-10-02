import java.util.Scanner;

public class isFibonacci {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scn = new Scanner(System.in);
		int counter = scn.nextInt();

		int a = 0;
		int b = 1;
		for (int i = 0; i < counter; i++) {
			System.out.println(a);
			int c = a + b;
			a = b;
			b = c;
		}
	}

}
