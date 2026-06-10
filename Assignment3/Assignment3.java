import java.util.ArrayList;
import java.util.Scanner;

public class Assignment3
{
    public static void main(String[] args)
    {
        ArrayList<String> books = new ArrayList<String>();

        books.add("Java Programming");
        books.add("Data Structures");
        books.add("Python Basics");
        books.add("Computer Networks");
        books.add("computer architecture");
        books.add("Operating System");

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a word to search:");
        String word = sc.nextLine();

        System.out.println("Matching books are:");

        for(int i = 0; i < books.size(); i++)
        {
            String title = books.get(i);

            if(title.toLowerCase().contains(word.toLowerCase()))
            {
                System.out.println(title);
            }
        }

        sc.close();
    }
}
