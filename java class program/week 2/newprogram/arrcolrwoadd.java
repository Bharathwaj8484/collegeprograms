class HelloWorld {
    public static void main(String[] args) {
        int[][] array = {
                         {2,5,1},
                         {6,7,4},
                         {1,8,6}
                          };
                          
    int  l = array.length;       
    int x[] = new int[4];
        
        for(int i = 0 ; i<3 ; i++){
            for(int j = 0 ; j<2 ; j++){
                if(array[i][j]<array[i][j+1]){
                    x[i] = array[i][j+1];
                } 
                else{
                    x[i] = array[i][j];
                }
            }
        }
        for(int i = l-1 ; i<l ; i++){
            for(int j = 0; j<l-1;j++ ){
                x[i] = array[i][j];
                
                if(x[i]<array[i][j+1]){
                    System.out.println(x[i]);
                    x[i] = array[i][j+1];
                    
                }
                
            }
        }
        
       /*for(int i =0 ; i<3;i++){
            System.out.println(x[i]);
        }*/
        
       int [][] fiar = new int [l][l+1];
       
       for(int i = 0 ; i<3 ; i++){
           for(int j = 0 ; j<4; j++){
               if(i<3 && j<3){
                   fiar[i][j]=array[i][j];
               } 
               else{
                   fiar[i][j] = x[i];
               }
           }
           
       }
       
       
         for(int i = 0 ; i<3 ; i++){
           for(int j = 0 ; j<4; j++){
              System.out.print(fiar[i][j]);
           }
           System.out.println(" ");
           
       }
       

        
        
    }
}