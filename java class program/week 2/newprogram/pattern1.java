public class pattern1 {
    public static void main(String args[]){
        int n=5,i,j,x=1;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(j<=n-i){
                    System.out.print(" ");
                }
                else{
                    System.out.print(x+" ");
                    if(x==n){
                        x=0;
                        x++;
                    }
                }
            }
            System.out.println(" ");
        }
    }
}
