public class JavaProgram6{
    public static void main(String[] args){
        int[] arr = {1,2,3,4,5,6,10,8,9};
        String result = Check_Sorted_Array(arr);
        System.out.println(result);
    }
    public static String Check_Sorted_Array(int[] arr){
        for(int i =1;i<arr.length;i++){
            if (arr[i-1]>arr[i])
                return "array not sorted";
        }
        return "array is sorted";
    }
    
}
