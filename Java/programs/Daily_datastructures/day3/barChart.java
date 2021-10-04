/*
 * bar chart
 * reverse array
 */
public class barChart {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[] arr = { 2, 3, 5, 0, 5, 7, 20 };
		reverse(arr);
		// barChart(arr);
		printArray(arr);

	}

	public static void printArray(int[] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}

	public static void barChart(int[] arr) {
		int max = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] > max) {
				max = arr[i];
			}
		}

		for (int i = max; i >= 1; i--) {
			for (int j = 0; j < arr.length; j++) {
				if (arr[j] >= i) {
					System.out.print("*");
				} else {
					System.out.print(" ");
				}
			}
			System.out.println();
		}

	}

	public static void reverse(int[] arr) {
		int i = 0;
		int j = arr.length - 1;
		while (i <= j) {
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}
	}

}
