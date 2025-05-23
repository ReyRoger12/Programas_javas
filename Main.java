import java.io.*;
import java_cup.runtime.*;

public class Main {
    public static void main(String[] args) {
        System.out.print("Ingrese una expresión matemática: ");
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String input = reader.readLine();

            Lexer lexer = new Lexer(new StringReader(input));
            parser parser = new parser(lexer);
            parser.parse();
            System.out.println("La expresión es sintácticamente correcta.");
        } catch (Exception e) {
            System.err.println("La expresión es incorrecta. " + e.getMessage());
        }
    }
}