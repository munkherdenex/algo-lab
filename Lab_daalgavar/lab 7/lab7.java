import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Lab7 {

    static class Item {
        double value;
        double weight;
        double ratio;

        public Item(double value, double weight) {
            this.value = value;
            this.weight = weight;
            this.ratio = value / weight;
        }
    }

    public static double fractionalKnapsack(double capacity, double[] weights, double[] values) {
        int n = weights.length;
        List<Item> items = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            items.add(new Item(values[i], weights[i]));
        }

        Collections.sort(items, new Comparator<Item>() {
            @Override
            public int compare(Item o1, Item o2) {
                return Double.compare(o2.ratio, o1.ratio);
            }
        });

        double maxValue = 0.0;

        for (Item item : items) {
            if (capacity >= item.weight) {
                maxValue += item.value;
                capacity -= item.weight;
            } else {
                maxValue += item.ratio * capacity;
                break;
            }
        }

        return maxValue;
    }

    public static void main(String[] args) {
        double[] weights = {10, 20, 30};
        double[] values = {60, 100, 120};
        double capacity = 50;

        System.out.println("Maximum value: " + fractionalKnapsack(capacity, weights, values));
    }
}
