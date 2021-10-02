public class countPrime {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int c = countPrimes(10);
		int m = countPrimeFaster(1000);
		System.out.printf("slow= %d, fast = %d", c, m);
	}

	public static int countPrimes(int n) {
		int c = 0;
		for (int i = 2; i <= n; i++) {
			if (isprime(i)) {
				c++;
			}
		}
		return c;
	}

	public static boolean isprime(int n) {
		boolean prime = true;
		for (int j = 2; j * j <= n; j++) {
			if (n % j == 0) {
				return false;
			}
		}
		return true;
	}

	public static int countPrimeFaster(int n) {
		int[] counter = new int[n];
		int primeCount = 0;
		for (int i = 2; i * i < n; i++) {
			if (counter[i] == 0) {
				for (int j = 2; j * i < n; j++) {
					if (counter[i * j] == 0) {
						counter[i * j] += 1;
					}
				}
			}
		}
		for (int i = 2; i < n; i++) {
			if (counter[i] == 0) {
				primeCount++;
			}

		}
		return primeCount;
	}
}
