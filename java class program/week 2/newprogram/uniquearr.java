import java.util.Arrays;

public class uniquearr{
    public static void main(String args[]){
        int[] a={10,20,30,40,10,20,50};
        int[] b = new int[10];
        int f=0;
        for(int i=0;i<a.length;i++){
            f=0;
            for(int j=0;j<a.length;j++){
                if (a[i]==a[j])
                    f=1;
                    break;
            }
            if (f==0)
                b = Arrays.copyOf(b, b.length + 1);
                b[b.length - 1] = a[i]; 
        }
        for(int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
    
}
}
}
