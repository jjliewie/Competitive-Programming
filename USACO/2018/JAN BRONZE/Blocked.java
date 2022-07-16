import java.io.*;
import java.util.*;

class Blocked{
    public static int area(int x1, int x2, int y1, int y2){
        int width = Math.abs(x1 - x2);
        int height = Math.abs(y1 - y2);

        return width * height;
    }

    public static int solution(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4){
        boolean tr = y4 >= y2 && x4 >= x2;
        boolean tl = x3 <= x1 && y4 >= y2;
        boolean br = x4 >= x2 && y3 <= y1;
        boolean bl = y3 <= y1 && x3 <= x1;

        if (tl && br) {
            return 0;
        }

        if (tr && tl || br && bl) {
            return area(x1, x2, y1, y3);
        }

        if (tr && br || bl && tl) {
            return area(x2, x4, y1, y2);
        }

        return area(x1, x2, y1, y2);
        
    }

    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader("billboard.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("billboard.out")));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        int x1 = Integer.parseInt(st.nextToken());
		int y1 = Integer.parseInt(st.nextToken());
		int x2 = Integer.parseInt(st.nextToken());
		int y2 = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(reader.readLine());
		int x3 = Integer.parseInt(st.nextToken());
		int y3 = Integer.parseInt(st.nextToken());
		int x4 = Integer.parseInt(st.nextToken());
		int y4 = Integer.parseInt(st.nextToken());

        int ans = solution(x1, y1, x2, y2, x3, y3, x4, y4);

        pw.println(ans);
        pw.close();
    }
}