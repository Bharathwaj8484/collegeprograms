public class mergearray {
    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {4, 5, 6, 7, 8};

        int totalLength = arr1.length + arr2.length;
        int[] mergedArray = new int[totalLength];
        int mergedIndex = 0;
        for (int num : arr1) {
            boolean isD = false;
            for (int mergedNum : mergedArray) {
                if (num == mergedNum) {
                    isD = true;
                    break;
                }
            }
            if (!isD) {
                mergedArray[mergedIndex++] = num;
            }
        }

        for (int num : arr2) {
            boolean isD = false;
            for (int mergedNum : mergedArray) {
                if (num == mergedNum) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                mergedArray[mergedIndex++] = num;
            }
        }

        int[] finalMergedArray = new int[mergedIndex];
        System.arraycopy(mergedArray, 0, finalMergedArray, 0, mergedIndex);

        System.out.println("Merged array with no duplicates:");
        for (int num : finalMergedArray) {
            System.out.print(num + " ");
        }
    }
}
