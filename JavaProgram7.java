public class JavaProgram7{
    public static void main(String[] args){
        // int n  = 5;
        // int result = Get_Sum(n);
        // System.out.println(result);
        // int factorial = Factorial(n);
        // System.out.println(factorial);
        // String a = "aabbaa";
        // boolean t = Check_Palindrom(a, 0, a.length()-1);
        // System.out.println(t);
        int max_cuts = max_rope_cut(23, 12, 9, 1);
        System.out.println(max_cuts);
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
    // public static boolean Check_Palindrom(String a,String start,String end,int n){
    //    if(start==end){
    //     return Check_Palindrom(a,a.charAt(a.length-n),a.charAt(n-1));
    //    }
    //    else
    //     return false;
    // return true;
    // }

    public static boolean Check_Palindrom(String a,int start,int end){
        if (start>=end)
            return true;
        return (a.charAt(start)==a.charAt(end))&&(Check_Palindrom(a,start+1,end-1));
    }
    public static int max_rope_cut(int n,int a,int b,int c){
        if(n==0) return 0;
        if(n<0) return -1;
        int res = Math.max(Math.max(max_rope_cut(n-a, a, b, c),max_rope_cut(n-b, a, b, c)),max_rope_cut(n-c, a, b, c));
        if (res==-1) return -1;
        return res+1;
    }
}
