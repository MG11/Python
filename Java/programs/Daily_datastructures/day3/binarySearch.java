import java.util.Scanner;

public class binarySearch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		binarySearch();
	}

	// O(logn)
	public static void binarySearch() {
		int position = -1;
		int[] arr = { 1, 2, 3, 4, 5 };
		Scanner scn = new Scanner(System.in);
		int e = scn.nextInt();
		int i = 0;
		int j = arr.length - 1;
		int mid = 0;
		while (i <= j) {
			mid = (i + j) / 2;
			if (e == arr[mid]) {
				position = mid;
				break;
			} else if (arr[mid] > e) {
				j = mid - 1;
			} else {
				i = mid + 1;
			}
		}
		System.out.println(position);
	}

}
