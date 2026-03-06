public class JavaProgram7{
    public static void main(String[] args){
        int n  = 10;
        int result = Get_Sum(n);
        System.out.println(result);
    }
    public static int Get_Sum(int n){
        if(n==0){
            return 0;
        }

        return n+Get_Sum(n-1);
    }
    
}
