import java.util.Scanner;

public class JavaProgram3 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        CountnoOfDigits(sc);
    }
     public static String CheckForPrime(int n){
        int x = n;
        for(int i = 2;i<=x;i++){
            if(n%i==0)
                return "it is not a prime";
            else{
                x = Math.abs(n/i);
            }
        }
        return "it is prime";  // there are 3 way by which we could do this but this was done by my own rest written in the book
    }
    public static int fibbonaci(int n){
        if(n<=1)
            return 1;
        return fibbonaci(n-1)+fibbonaci(n-2);
    }
    public static void CountnoOfDigits(Scanner sc){
        System.out.print("enter the digit u want--");
        String x = sc.nextLine();
        System.out.println(x.length());
        System.out.println("by while loop enter the digit again here--");
        int n = sc.nextInt();
        int count = 0;
        while (n!=0) {
            n = Math.abs(n/10);
            count+=1;
        }
        System.out.println(count); //two methods for this one is the string method and other is the looping method O(1) and O(n)
    }
    
}
