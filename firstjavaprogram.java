import java.util.Scanner;

public class firstjavaprogram {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = 5;
        Swapping();
        SumofNnos(sc);
        sc.close();
    }
    public static void Swapping(){
        //swapping of two no.s
        int a= 10,b = 20;
        System.out.printf("value of a is %d value of b is %d\n",a,b);
        //no one line swapping in java unlike python
        //methods - temp meth, a=a+b->b=a-b->a=a-b (can cause int overflow), or using xor method below
        a = a^b;
        System.out.println(a+" "+b);
        b = a^b;
        System.out.println(a+" "+b);
        a = a^b;
        System.out.println(a+" "+b);
    }
    public static void SumofNnos(Scanner sc){
        int sum = 0;
        System.out.printf("enetr the no. of natural no.s u want--");
        int n = sc.nextInt();
        for(int i =1;i<=n;i++){
            sum += i;
        }
        System.out.println(sum);
        sc.close(); // this program has O(n) but with direct formula we can have O(1)
    }
}
