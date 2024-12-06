class Lab10 {

    public static int calculateTotalCost(int n) {
        int totalCost = 0;

        for (int i = 1; i <= n; i++) {
            if ((i & (i - 1)) == 0) { 
                totalCost += i;      
            } else {
                totalCost += 1;      
            }
        }

        return totalCost;
    }

    public static void main(String[] args) {
        int n = 10;
        int totalCost = calculateTotalCost(n);
        System.out.println("Total cost for " + n + " operations is: " + totalCost);
    }
}
