class noneight{
public static void main(String args[]){
    int i=4858658;
    int e=0,f=0;
    while(i>0){
        int r= i%10;
        if (r!=8){
            f=f+r*10;
        }
        else{
            e = e+i*10;
        }
        i=i/10;
    }
    System.out.println(e);
}}