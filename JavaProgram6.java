import java.util.Arrays;

public class JavaProgram6{
    public static void main(String[] args){
        int[] arr = {1,2,3,4,4,5,5,5,6,7,7,8,9,10,11,11,16};
        //String result = Check_Sorted_Array(arr);
        //System.out.println(result);
        int size = RemDup(arr,17 );
        System.out.println(Arrays.toString(arr));
        System.out.println("size is--"+size);
    }
    public static String Check_Sorted_Array(int[] arr){
        for(int i =1;i<arr.length;i++){
            if (arr[i-1]>arr[i])
                return "array not sorted";
        }
        return "array is sorted";
    }
    public static int RemDup(int[] arr,int n){
        int temp[] = new int[n];
        temp[0] = arr[0];
        int res = 1;
        for(int i=0;i<n;i++){
            if(temp[res-1]!=arr[i]){
                temp[res] = arr[i];
                res++;
            }
        }
        for (int i=0;i<res;i++)
            arr[i] = temp[i];
        return res;
    }
    
}
