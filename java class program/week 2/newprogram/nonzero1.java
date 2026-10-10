public class nonzero1{
    public static void main(String args[]){
        int n=0,z=0;
        int[] arr={0,2,1,7,0,5,0,8};
        int len=arr.length;
        while(n<len){
            if(arr[n]!=0){
                int temp=arr[n];
                arr[n]=arr[z];
                arr[z]=temp;
                n++;
                z++;
        }
            else
                n++;
}
        for(int i=0;i<len;i++)
            System.out.print(arr[i]+" ");
}}