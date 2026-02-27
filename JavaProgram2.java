import java.util.Scanner;

public class JavaProgram2 {
    public static void main(String[] args){
        Findonesdigit();
    }
    public static void Findonesdigit(){
        System.out.println("enter any no. to get the last digit of ur no.--");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        System.out.println(x%10);
        sc.close();
    }
    public static void Largestof3(int a,int b,int c){
        if(a<b && c<b)
            System.out.println(b+" is the greatest");
        else if(a>b && a>c)
            System.out.println(a+" is the greatest value");
        else
            System.out.println(c+" is the greatest");
    }
    public static void CheckLeapYear(Scanner sc){
        System.out.printf("enter the year u need");
        int x = sc.nextInt();
        if(x%100 == 0){
            if(x%400==0)
                System.out.println("it is a leap year");
            else
                System.out.println("it is not a leap year");
        }
        else if(x%4==0)
            System.out.println("it is a leap year");
        sc.close();
    }
    public static int FactorialOfN(int n){
        if(n<0){
            System.err.println("error: cannot compute factorial for negative values");
            return -1;}
        else if(n==0)
            return 1;
        
        return (n)*FactorialOfN(n-1);
    }
}

