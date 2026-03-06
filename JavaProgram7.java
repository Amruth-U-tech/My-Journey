public class JavaProgram7{
    public static void main(String[] args){
        int n  = 5;
        int result = Get_Sum(n);
        System.out.println(result);
        int factorial = Factorial(n);
        System.out.println(factorial);
    }
    public static int Get_Sum(int n){
        if(n==0){
            return 0;
        }

        return n+Get_Sum(n-1);
    }
    public static int Factorial(int n){
        if (n<0){
            System.out.println("cannot get factorial of negative no.s");
        }
        else if(n==0){
            return 1;
        }
        return n*Factorial(n-1);
    }
}
