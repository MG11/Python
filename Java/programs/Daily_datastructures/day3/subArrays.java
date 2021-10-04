
public class subArrays {

	public static int[][] SubArrays(int[] arr, int idx) {
		if (arr.length == idx) {
			int[][] ans = { { 0 } };
			return ans;
		}
		int[][] smallAns = SubArrays(arr, idx + 1);

		int ans[][] = new int[2 * smallAns.length][];
		for (int i = 0; i < smallAns.length; i++) {
			ans[i] = smallAns[i];
		}
		for (int i = 0; i < smallAns.length; i++) {
			int[] a1 = new int[smallAns[i].length + 1];
			a1[0] = arr[idx];
			for (int j = 1; j < smallAns[i].length + 1; j++) {
				a1[j] = smallAns[i][j - 1];
			}
			ans[i + smallAns.length] = a1;
		}
		return ans;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = { 1, 2, 3, 4 };
		int[][] ans = SubArrays(arr, 0);
		for (int i = 0; i < ans.length; i++) {
			for (int j = 0; j < ans[i].length; j++) {
				System.out.print(ans[i][j] + ",");
			}
			System.out.println();
		}
	}

}
