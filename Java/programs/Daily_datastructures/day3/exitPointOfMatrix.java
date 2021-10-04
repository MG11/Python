
public class exitPointOfMatrix {

	public static void main(String[] args) {
		int arr[][] = { { 0, 0, 1, 0 }, { 1, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 1, 0 }, };
		int i = 0;
		int j = 0;
		int dir = 0;
		while (true) {
			dir = (dir + arr[i][j]) % 4;
			switch (dir) {
			case 0:
				i++;
				if (i == arr[0].length) {
					i--;
					System.out.printf("%d %d", i, j);
					return;
				}
				break;
			case 1:
				j++;
				if (j == arr.length) {
					j--;
					System.out.printf("%d %d", i, j);
					return;
				}
				break;
			case 2:
				i--;
				if (i == -1) {
					i++;
					System.out.printf("%d %d", i, j);
					return;
				}
				break;
			case 3:
				j--;
				if (j == -1) {
					j++;
					System.out.printf("%d %d", i, j);
					return;
				}
				break;
			}
		}

	}

}
