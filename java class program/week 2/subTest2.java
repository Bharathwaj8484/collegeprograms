class subtest2 {
    public static void main(String[] args) {
        int[][] marks = {
            {123, 20, 30, 47, 90},
            {535, 10, 40, 41, 91},
            {213, 10, 20, 30, 60},
            {975, 25, 25, 25, 75}
        };

        // Task 1: Find the highest marks for each subject and print them
        for (int subject = 1; subject <= 4; subject++) {
            int highestMark = 0;
            int highestRollNo = 0;
            
            for (int[] student : marks) {
                if (student[subject] > highestMark) {
                    highestMark = student[subject];
                    highestRollNo = student[0];
                }
            }
            
            System.out.println("Highest mark in subject " + subject + ": " + highestMark + " (Roll No: " + highestRollNo + ")");
        }

        // Task 2: Find the person who got the highest total marks and print their roll number
        int highestTotal = -1;
        int highestTotalRollNo = -1;

        for (int[] student : marks) {
            int totalMarks = student[1] + student[2] + student[3] + student[4];
            
            if (totalMarks > highestTotal) {
                highestTotal = totalMarks;
                highestTotalRollNo = student[0];
            }
        }

        System.out.println("Roll No of student with highest total marks: " + highestTotalRollNo);
    }
}
