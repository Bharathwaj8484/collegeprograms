public class movezero{
    public static void main(String args[]){
        int[] a={10,20,30,20,10};
        int d=-1,i,j;
        for (i=0;i<a.length;i++){
            for (j=i+1;j<a.length;j++){
                if (a[i]==a[j] && (j-i>d)){
                    d=j-i;
                }
        }
    }
    System.out.println("The distance: "+d);
    
}
}
