
import java.util.ArrayList;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;
import java.io.File;


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
        // file reading
        try{
            FileReader myObj = new FileReader("myjavafile.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);

                
            }
            myReader.close();
        } catch (FileNotFoundException e){
            System.out.println("An error occurred");
            e.printStackTrace();

        }


        // Delete file


        File myFile = new File("myjavafile.txt");
        if (myFile.delete()){
            System.out.println("Deleted the file: "+myFile.getName());

        }else{
            System.out.println("Failed to delete the file");
        }


        // counting words


        String words = "this is thejava programming language";
        int countWords = words.split("\\s").length;
        System.out.println(countWords);

        // Reverse a string

    String orginal = "Hello World!";
    String reverse = "";

    System.out.println("Orginal String: "+orginal);

    for (int i = 0;i<orginal.length(); i++){
        reverse = orginal.charAt(i)+reverse;
        
    }
    System.out.println("Reversed string: "+reverse);

    }

    
}