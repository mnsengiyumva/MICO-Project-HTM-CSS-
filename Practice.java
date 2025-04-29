
import java.util.ArrayList;
import java.io.FileWriter;
import java.io.IOException;

public class Practice {

    public static void main(String[] args){
        System.out.println("Hello world");

        // if statements
        ArrayList<String> names = new ArrayList<String>();
        names.add("Mico");
        names.add("Billy");
        names.add("Tom");
        System.out.println(names);

        // File handling ---> Writing a file

        try{
            FileWriter myFile = new FileWriter("myjavafile.txt");
            myFile.write("This is my first java file, out of more I will creat.");
            myFile.close();
            System.out.println("Files written Successfully");


        } catch(IOException e){
            System.out.println("An Error occured");
            e.printStackTrace();
        }







    }
}