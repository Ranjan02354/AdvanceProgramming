import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

class Student {

    private int id;
    private String name;
    private List<String> courses;
    private Map<String, Integer> scores;

    public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    public List<String> getCourses() {
        return courses;
    }

    public Map<String, Integer> getScores() {
        return scores;
    }

    // Calculate average score using getOrDefault
    public double getAverageScore() {
        if (courses.isEmpty()) {
            return 0;
        }

        return courses.stream()
                .mapToInt(course -> scores.getOrDefault(course, 0))
                .average()
                .orElse(0);
    }

    @Override
    public String toString() {
        return id + " " + name + " Avg: " + getAverageScore();
    }
}

public class Assignment6 {

    public static List<Student> getTopNStudents(List<Student> students, int n) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

    // Calculate average score for each course
    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Set<String> courses = getAllUniqueCourses(students);
        Map<String, Double> averageScores = new HashMap<>();

        for (String course : courses) {
            double avg = students.stream()
                    .mapToInt(student -> student.getScores().getOrDefault(course, 0))
                    .average()
                    .orElse(0);

            averageScores.put(course, avg);
        }

        return averageScores;
    }

    // Get all unique courses
    public static Set<String> getAllUniqueCourses(List<Student> students) {
        return students.stream()
                .flatMap(student -> student.getCourses().stream())
                .collect(Collectors.toSet());
    }

    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();

        List<String> courses1 = Arrays.asList("Math", "CS");
        Map<String, Integer> scores1 = new HashMap<>();
        scores1.put("Math", 90);
        scores1.put("CS", 95);

        students.add(new Student(1, "Ranjan", courses1, scores1));

        List<String> courses2 = Arrays.asList("Math", "Physics");
        Map<String, Integer> scores2 = new HashMap<>();
        scores2.put("Math", 80);
        scores2.put("Physics", 85);

        students.add(new Student(2, "Rahul", courses2, scores2));

        System.out.println("Top Students:");
        getTopNStudents(students, 2).forEach(System.out::println);

        System.out.println("\nAverage Score Per Course:");
        System.out.println(getAverageScorePerCourse(students));

        System.out.println("\nUnique Courses:");
        System.out.println(getAllUniqueCourses(students));
    }
}