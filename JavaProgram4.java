import java.util.Scanner;
//there are multiple ways to find max in array forloop,sorting and then collecting last element
//then there isstream method and collections.map method excepting for sorting all has O(n) time
//but looping is best in java because other methods might be modern but carry overhead.

public class JavaProgram4 {
    public static void main(String[] args){
        int[] arr = new int[4];
        Scanner sc = new Scanner(System.in);
        int[] Filled_Array = Filling_Array(sc, arr);
        int max = Max_in_array(Filled_Array);
        System.out.println("max no. is--"+max);
    }
    public static int[] Filling_Array(Scanner sc,int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.printf("enter the no. for %d--",i);
            arr[i] = sc.nextInt();
        }
        return arr;
    }
    public static int Max_in_array(int[] arr){
        int max = arr[0];
        for(int i=1;i<4;i++){
            if(arr[i]>max)
                max = arr[i];
        }
        return max;
    }
}
