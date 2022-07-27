import java.util.*;

public class Main {
    public static void main(String [] args) {
        Map<Long, Long> m = new HashMap<Long, Long>();
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        for(int i = 0; i < n; i++) {
            int q = scan.nextInt();
            if (q == 0) {
                m.put(scan.nextLong(), scan.nextLong());
                continue;
            }
            long key = scan.nextLong();
            if(m.containsKey(key)) {
                System.out.println(m.get(key));
            }
            else { System.out.println(0); }
        }
        scan.close();
    }
}