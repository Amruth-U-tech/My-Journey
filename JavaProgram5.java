public class JavaProgram5{
    public static void main(String[] args){
        int[] arr = {1,2,3,4,5,6,7,8,9};
        int[] r = ReversingArray(arr);
        System.out.println("new arr is-"+r);
    }
    public static int[] ReversingArray(int[] arr){
        for(int i=0;i<Math.abs(arr.length/2);i++){
            int temp = arr[-(i+1)];
            arr[-(i+1)]  = arr[i];
            arr[i]=temp;
        }
        return arr;
    }
    
}
